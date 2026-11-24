"""
Week 1, Day 1: Python for AWS Lambda
Exercises focused on Lambda-specific Python patterns

These exercises simulate Lambda development patterns.
Run them locally to understand the concepts before deploying to AWS.
"""

import json
import os
from datetime import datetime
from typing import Dict, Any


def exercise_1_lambda_handler_pattern():
    """
    Understand the basic Lambda handler pattern.
    
    In AWS Lambda, every function has a handler function that takes
    two parameters: event and context.
    
    event: Dict containing input data (varies by trigger)
    context: Object with runtime information about the Lambda function
    """
    
    # Simulate a Lambda handler
    def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
        """
        Basic Lambda handler - this is what AWS Lambda executes.
        
        Args:
            event: Input data from the trigger (API Gateway, S3, etc.)
            context: Runtime information (not used in this example)
        
        Returns:
            Dict containing response data
        """
        # Extract data from event (common pattern)
        name = event.get('name', 'AWS Lambda User')
        user_id = event.get('userId', 'unknown')
        
        # Business logic
        greeting = f"Hello {name}! (User ID: {user_id})"
        timestamp = datetime.utcnow().isoformat()
        
        # Return response (API Gateway expects specific format)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'X-Custom-Header': 'Lambda-Exercise'
            },
            'body': json.dumps({
                'message': greeting,
                'timestamp': timestamp,
                'inputEvent': event
            })
        }
    
    # Test with different event patterns
    print("Exercise 1: Lambda Handler Patterns")
    print("=" * 50)
    
    # Test 1: API Gateway event
    api_event = {
        'httpMethod': 'GET',
        'path': '/hello',
        'queryStringParameters': {'name': 'Bo', 'userId': '123'},
        'headers': {'User-Agent': 'TestClient'},
        'body': None
    }
    
    result1 = lambda_handler(api_event, None)
    print("\nTest 1 - API Gateway Event:")
    print(f"Response: {json.dumps(result1, indent=2)}")
    
    # Test 2: Direct invocation (testing)
    test_event = {
        'name': 'TestUser',
        'userId': 'test-456',
        'action': 'greet'
    }
    
    result2 = lambda_handler(test_event, None)
    print("\nTest 2 - Direct Invocation:")
    print(f"Response: {json.dumps(result2, indent=2)}")
    
    # Test 3: Missing parameters (should use defaults)
    minimal_event = {}
    
    result3 = lambda_handler(minimal_event, None)
    print("\nTest 3 - Minimal Event (default values):")
    print(f"Response: {json.dumps(result3, indent=2)}")
    
    return lambda_handler


def exercise_2_environment_variables():
    """
    Learn to use environment variables in Lambda.
    
    Environment variables are essential for configuration in Lambda:
    - Database connections
    - API keys
    - Feature flags
    - Environment-specific settings
    """
    
    def lambda_handler_with_env(event, context):
        """
        Lambda handler using environment variables.
        """
        # Get environment variables (with defaults)
        stage = os.environ.get('STAGE', 'dev')
        api_version = os.environ.get('API_VERSION', 'v1')
        debug_mode = os.environ.get('DEBUG_MODE', 'false').lower() == 'true'
        
        # Business logic using env vars
        response_data = {
            'stage': stage,
            'apiVersion': api_version,
            'debugEnabled': debug_mode,
            'region': os.environ.get('AWS_REGION', 'us-east-1'),
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Add extra debug info if enabled
        if debug_mode:
            response_data['environmentVars'] = dict(os.environ)
            response_data['eventDetails'] = {
                'keys': list(event.keys()),
                'type': type(event).__name__
            }
        
        return {
            'statusCode': 200,
            'body': json.dumps(response_data)
        }
    
    print("\n\nExercise 2: Environment Variables")
    print("=" * 50)
    
    # Set environment variables (simulating Lambda environment)
    original_env = os.environ.copy()
    
    try:
        # Test 1: Default values
        os.environ.clear()
        result1 = lambda_handler_with_env({}, None)
        print("\nTest 1 - No Environment Variables Set:")
        print(f"Response: {json.dumps(json.loads(result1['body']), indent=2)}")
        
        # Test 2: Production configuration
        os.environ.update({
            'STAGE': 'production',
            'API_VERSION': 'v2',
            'DEBUG_MODE': 'false',
            'AWS_REGION': 'us-west-2'
        })
        
        result2 = lambda_handler_with_env({'action': 'test'}, None)
        print("\nTest 2 - Production Configuration:")
        print(f"Response: {json.dumps(json.loads(result2['body']), indent=2)}")
        
        # Test 3: Debug configuration
        os.environ['DEBUG_MODE'] = 'true'
        result3 = lambda_handler_with_env({'test': 'data', 'user': 'admin'}, None)
        print("\nTest 3 - Debug Mode Enabled:")
        debug_response = json.loads(result3['body'])
        # Don't print full env for brevity
        debug_response['environmentVars'] = {'truncated': '...'}
        print(f"Response: {json.dumps(debug_response, indent=2)}")
        
    finally:
        # Restore original environment
        os.environ.clear()
        os.environ.update(original_env)
    
    return lambda_handler_with_env


def exercise_3_error_handling():
    """
    Learn error handling patterns for Lambda.
    
    Important considerations:
    - Lambda should always return a response (even for errors)
    - Log errors to CloudWatch
    - Use try-except blocks appropriately
    - Return meaningful error messages to clients
    """
    
    class LambdaError(Exception):
        """Custom exception for Lambda errors."""
        pass
    
    def lambda_handler_with_errors(event, context):
        """
        Lambda handler with comprehensive error handling.
        """
        try:
            # Validate input
            if not event.get('operation'):
                raise LambdaError("Missing required field: 'operation'")
            
            operation = event['operation']
            data = event.get('data', {})
            
            # Business logic with potential errors
            if operation == 'divide':
                numerator = data.get('numerator', 0)
                denominator = data.get('denominator', 1)
                
                if denominator == 0:
                    raise LambdaError("Division by zero is not allowed")
                
                result = numerator / denominator
                response = {'result': result}
                
            elif operation == 'parse_json':
                json_str = data.get('json_string', '{}')
                parsed = json.loads(json_str)
                response = {'parsed': parsed}
                
            elif operation == 'get_env':
                key = data.get('key', '')
                if not key:
                    raise LambdaError("Missing key for environment variable")
                
                value = os.environ.get(key)
                if value is None:
                    raise LambdaError(f"Environment variable '{key}' not found")
                
                response = {key: value}
                
            else:
                raise LambdaError(f"Unknown operation: {operation}")
            
            # Success response
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'success': True,
                    'data': response,
                    'timestamp': datetime.utcnow().isoformat()
                })
            }
            
        except LambdaError as e:
            # Business logic error - return to client
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'success': False,
                    'error': str(e),
                    'errorType': 'ValidationError',
                    'timestamp': datetime.utcnow().isoformat()
                })
            }
            
        except json.JSONDecodeError as e:
            # JSON parsing error
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'success': False,
                    'error': f'Invalid JSON: {str(e)}',
                    'errorType': 'ParseError',
                    'timestamp': datetime.utcnow().isoformat()
                })
            }
            
        except Exception as e:
            # Unexpected error - log and return generic message
            # In real Lambda, this would log to CloudWatch
            print(f"UNEXPECTED ERROR: {type(e).__name__}: {str(e)}")
            
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'success': False,
                    'error': 'Internal server error',
                    'errorType': 'InternalError',
                    'timestamp': datetime.utcnow().isoformat()
                })
            }
    
    print("\n\nExercise 3: Error Handling in Lambda")
    print("=" * 50)
    
    # Set up test environment
    os.environ['TEST_KEY'] = 'test_value'
    
    test_cases = [
        {
            'name': 'Successful division',
            'event': {'operation': 'divide', 'data': {'numerator': 10, 'denominator': 2}},
            'expected_status': 200
        },
        {
            'name': 'Division by zero',
            'event': {'operation': 'divide', 'data': {'numerator': 10, 'denominator': 0}},
            'expected_status': 400
        },
        {
            'name': 'Valid JSON parsing',
            'event': {'operation': 'parse_json', 'data': {'json_string': '{"name": "Bo", "age": 30}'}},
            'expected_status': 200
        },
        {
            'name': 'Invalid JSON parsing',
            'event': {'operation': 'parse_json', 'data': {'json_string': '{invalid json}'}},
            'expected_status': 400
        },
        {
            'name': 'Get existing env var',
            'event': {'operation': 'get_env', 'data': {'key': 'TEST_KEY'}},
            'expected_status': 200
        },
        {
            'name': 'Get non-existent env var',
            'event': {'operation': 'get_env', 'data': {'key': 'NON_EXISTENT'}},
            'expected_status': 400
        },
        {
            'name': 'Missing operation',
            'event': {'data': {'some': 'data'}},
            'expected_status': 400
        },
        {
            'name': 'Unknown operation',
            'event': {'operation': 'unknown_op', 'data': {}},
            'expected_status': 400
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = lambda_handler_with_errors(test['event'], None)
        status_match = result['statusCode'] == test['expected_status']
        
        print(f"\nTest {i}: {test['name']}")
        print(f"  Event: {test['event']}")
        print(f"  Status: {result['statusCode']} (Expected: {test['expected_status']}) {'✓' if status_match else '✗'}")
        
        response_body = json.loads(result['body'])
        if response_body.get('success'):
            print(f"  Result: {response_body.get('data', {})}")
        else:
            print(f"  Error: {response_body.get('error')}")
    
    # Clean up
    del os.environ['TEST_KEY']
    
    return lambda_handler_with_errors


def exercise_4_logging_and_monitoring():
    """
    Learn logging patterns for CloudWatch monitoring.
    
    Best practices:
    - Use structured logging (JSON format)
    - Log at appropriate levels (INFO, WARN, ERROR)
    - Include correlation IDs for tracing
    - Don't log sensitive data
    """
    
    import logging
    
    class StructuredLogger:
        """Simple structured logger for Lambda."""
        
        def __init__(self, correlation_id=None):
            self.correlation_id = correlation_id or f"req-{datetime.utcnow().timestamp()}"
            self.logger = logging.getLogger(__name__)
            
            if not self.logger.handlers:
                handler = logging.StreamHandler()
                formatter = logging.Formatter(
                    '%(message)s'  # We'll format as JSON ourselves
                )
                handler.setFormatter(formatter)
                self.logger.addHandler(handler)
                self.logger.setLevel(logging.INFO)
        
        def _log(self, level: str, message: str, extra: Dict = None):
            """Log structured message."""
            log_entry = {
                'timestamp': datetime.utcnow().isoformat(),
                'level': level,
                'correlationId': self.correlation_id,
                'message': message,
                **(extra or {})
            }
            self.logger.info(json.dumps(log_entry))
        
        def info(self, message: str, extra: Dict = None):
            self._log('INFO', message, extra)
        
        def warn(self, message: str, extra: Dict = None):
            self._log('WARN', message, extra)
        
        def error(self, message: str, extra: Dict = None):
            self._log('ERROR', message, extra)
        
        def metric(self, name: str, value: float, unit: str = 'Count', extra: Dict = None):
            """Log a custom metric."""
            metric_data = {
                'metricName': name,
                'value': value,
                'unit': unit,
                '_aws': {
                    'Timestamp': int(datetime.utcnow().timestamp() * 1000),
                    'CloudWatchMetrics': [{
                        'Namespace': 'LambdaExercises',
                        'Dimensions': [['FunctionName', 'CorrelationId']],
                        'Metrics': [{'Name': name, 'Unit': unit}]
                    }]
                }
            }
            self._log('METRIC', f'Custom metric: {name}', {**metric_data, **(extra or {})})
    
    def lambda_handler_with_logging(event, context):
        """
        Lambda handler with structured logging.
        """
        # Extract correlation ID from event or generate
        correlation_id = event.get('requestId', event.get('correlationId'))
        logger = StructuredLogger(correlation_id)
        
        logger.info("Lambda execution started", {
            'eventType': type(event).__name__,
            'eventKeys': list(event.keys()),
            'functionName': context.function_name if hasattr(context, 'function_name') else 'local_test',
            'memoryLimit': context.memory_limit_in_mb if hasattr(context, 'memory_limit_in_mb') else 128
        })
        
        try:
            # Business logic
            operation = event.get('operation', 'unknown')
            data = event.get('data', {})
            
            logger.info(f"Processing operation: {operation}", {
                'operation': operation,
                'dataSize': len(str(data))
            })
            
            # Simulate some work
            if operation == 'process':
                items = data.get('items', [])
                processed = len(items)
                
                logger.metric('ItemsProcessed', processed)
                logger.info(f"Processed {processed} items")
                
                result = {'processed': processed}
                
            elif operation == 'validate':
                # Simulate validation
                is_valid = data.get('isValid', False)
                
                if not is_valid:
                    logger.warn("Validation failed", {
                        'data': data,
                        'reason': 'Invalid flag set to false'
                    })
                    raise ValueError("Data validation failed")
                
                logger.info("Validation passed")
                result = {'valid': True}
                
            else:
                logger.error(f"Unknown operation: {operation}")
                raise ValueError(f"Unknown operation: {operation}")
            
            # Success
            logger.info("Lambda execution completed successfully", {
                'result': result,
                'durationMs': 150  # Simulated
            })
            
            logger.metric('SuccessCount', 1)
            
            return {
                'statusCode': 200,
                'headers': {
                    'X-Correlation-Id': logger.correlation_id
                },
                'body': json.dumps({
                    'success': True,
                    'data': result,
                    'correlationId': logger.correlation_id
                })
            }
            
        except Exception as e:
            # Log error
            logger.error(f"Lambda execution failed: {str(e)}", {
                'errorType': type(e).__name__,
                'stackTrace': '...'  # In real code, would include traceback
            })
            
            logger.metric('ErrorCount', 1)
            
            return {
                'statusCode': 500,
                'headers': {
                    'X-Correlation-Id': logger.correlation_id
                },
                'body': json.dumps({
                    'success': False,
                    'error': str(e),
                    'correlationId': logger.correlation_id
                })
            }
    
    print("\n\nExercise 4: Logging and Monitoring")
    print("=" * 50)
    
    # Create mock context object
    class MockContext:
        function_name = 'test-lambda-function'
        memory_limit_in_mb = 256
        aws_request_id = 'test-request-123'
    
    mock_context = MockContext()
    
    # Test cases
    test_events = [
        {
            'name': 'Successful processing',
            'event': {
                'operation': 'process',
                'data': {'items': [1, 2, 3, 4, 5]},
                'requestId': 'req-123'
            }
        },
        {
            'name': 'Validation passed',
            'event': {
                'operation': 'validate',
                'data': {'isValid': True},
                'correlationId': 'corr-456'
            }
        },
        {
            'name': 'Validation failed',
            'event': {
                'operation': 'validate',
                'data': {'isValid': False}
            }
        },
        {
            'name': 'Unknown operation',
            'event': {
                'operation': 'unknown'
            }
        }
    ]
    
    for test in test_events:
        print(f"\nTest: {test['name']}")
        print(f"Event: {test['event']}")
        
        result = lambda_handler_with_logging(test['event'], mock_context)
        response = json.loads(result['body'])
        
        print(f"Status: {result['statusCode']}")
        print(f"Success: {response['success']}")
        print(f"Correlation ID: {response['correlationId']}")
        
        if response['success']:
            print(f"Result: {response.get('data', {})}")
        else:
            print(f"Error: {response.get('error')}")
    
    return lambda_handler_with_logging


def mini_project_simple_api_lambda():
    """
    Mini Project: Build a simple API Lambda handler.
    
    This simulates a Lambda behind API Gateway that:
    1. Handles different HTTP methods
    2. Validates input
    3. Returns appropriate responses
    4. Includes logging and error handling
    """
    
    print("\n" + "=" * 60)
    print("Mini Project: Simple API Lambda Handler")
    print("=" * 60)
    
    def api_lambda_handler(event, context):
        """
        Handle API Gateway requests.
        
        Expected event format (API Gateway Proxy):
        {
          "httpMethod": "GET|POST|PUT|DELETE",
          "path": "/resource",
          "queryStringParameters": {"param": "value"},
          "headers": {"Content-Type": "application/json"},
          "body": "JSON string or null"
        }
        """
        # Parse HTTP method
        http_method = event.get('httpMethod', 'GET').upper()
        path = event.get('path', '/')
        
        # Parse query parameters
        query_params = event.get('queryStringParameters', {}) or {}
        
        # Parse body if present
        body = {}
        if event.get('body'):
            try:
                body = json.loads(event['body'])
            except json.JSONDecodeError:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Invalid JSON in request body'})
                }
        
        # Route based on method and path
        if http_method == 'GET' and path == '/health':
            return handle_health_check()
        
        elif http_method == 'GET' and path == '/users':
            return handle_get_users(query_params)
        
        elif http_method == 'POST' and path == '/users':
            return handle_create_user(body)
        
        elif http_method == 'GET' and path.startswith('/users/'):
            user_id = path.split('/')[-1]
            return handle_get_user(user_id)
        
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': f'Route {http_method} {path} not found'})
            }
    
    def handle_health_check():
        """Health check endpoint."""
        return {
            'statusCode': 200,
            'body': json.dumps({
                'status': 'healthy',
                'timestamp': datetime.utcnow().isoformat(),
                'service': 'UserAPI'
            })
        }
    
    def handle_get_users(query_params):
        """Get list of users with optional filtering."""
        # In real Lambda, this would query a database
        # For demo, return mock data
        
        limit = int(query_params.get('limit', 10))
        offset = int(query_params.get('offset', 0))
        
        # Mock user data
        mock_users = [
            {'id': f'user-{i}', 'name': f'User {i}', 'email': f'user{i}@example.com'}
            for i in range(1, 101)
        ]
        
        # Apply pagination
        users = mock_users[offset:offset + limit]
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'users': users,
                'pagination': {
                    'limit': limit,
                    'offset': offset,
                    'total': len(mock_users),
                    'hasMore': offset + limit < len(mock_users)
                }
            })
        }
    
    def handle_create_user(body):
        """Create a new user."""
        # Validate required fields
        required_fields = ['name', 'email']
        missing_fields = [field for field in required_fields if field not in body]
        
        if missing_fields:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Missing required fields',
                    'missing': missing_fields
                })
            }
        
        # Validate email format (simple check)
        email = body['email']
        if '@' not in email:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Invalid email format'
                })
            }
        
        # In real Lambda, this would save to database
        # For demo, return success with generated ID
        user_id = f"user-{int(datetime.utcnow().timestamp())}"
        
        new_user = {
            'id': user_id,
            'name': body['name'],
            'email': body['email'],
            'createdAt': datetime.utcnow().isoformat()
        }
        
        # Add optional fields if provided
        if 'age' in body:
            new_user['age'] = body['age']
        
        return {
            'statusCode': 201,
            'headers': {
                'Location': f'/users/{user_id}'
            },
            'body': json.dumps({
                'message': 'User created successfully',
                'user': new_user
            })
        }
    
    def handle_get_user(user_id):
        """Get a specific user by ID."""
        # In real Lambda, this would query database
        # For demo, return mock data or 404
        
        if not user_id.startswith('user-'):
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'User not found'})
            }
        
        # Mock user data
        user = {
            'id': user_id,
            'name': 'Demo User',
            'email': 'demo@example.com',
            'createdAt': '2024-01-01T00:00:00Z'
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps({'user': user})
        }
    
    # Test the API handler
    print("\nTesting API Lambda Handler...")
    
    test_cases = [
        {
            'name': 'Health Check',
            'event': {'httpMethod': 'GET', 'path': '/health'}
        },
        {
            'name': 'Get Users (default pagination)',
            'event': {'httpMethod': 'GET', 'path': '/users'}
        },
        {
            'name': 'Get Users (with pagination)',
            'event': {
                'httpMethod': 'GET',
                'path': '/users',
                'queryStringParameters': {'limit': '5', 'offset': '10'}
            }
        },
        {
            'name': 'Create User (success)',
            'event': {
                'httpMethod': 'POST',
                'path': '/users',
                'body': json.dumps({
                    'name': 'Bo',
                    'email': 'bo@example.com',
                    'age': 30
                })
            }
        },
        {
            'name': 'Create User (missing fields)',
            'event': {
                'httpMethod': 'POST',
                'path': '/users',
                'body': json.dumps({'name': 'Bo'})  # Missing email
            }
        },
        {
            'name': 'Create User (invalid email)',
            'event': {
                'httpMethod': 'POST',
                'path': '/users',
                'body': json.dumps({
                    'name': 'Bo',
                    'email': 'invalid-email'
                })
            }
        },
        {
            'name': 'Get Specific User',
            'event': {'httpMethod': 'GET', 'path': '/users/user-123'}
        },
        {
            'name': 'Get Non-existent User',
            'event': {'httpMethod': 'GET', 'path': '/users/123'}  # Doesn't start with 'user-'
        },
        {
            'name': 'Unknown Route',
            'event': {'httpMethod': 'GET', 'path': '/unknown'}
        }
    ]
    
    for test in test_cases:
        print(f"\n{'─' * 50}")
        print(f"Test: {test['name']}")
        print(f"Method: {test['event'].get('httpMethod')}")
        print(f"Path: {test['event'].get('path')}")
        
        result = api_lambda_handler(test['event'], None)
        response = json.loads(result['body'])
        
        print(f"Status: {result['statusCode']}")
        
        if result['statusCode'] == 200 or result['statusCode'] == 201:
            print("Response: Success")
            if 'user' in response:
                print(f"  User: {response['user'].get('id')}")
            elif 'users' in response:
                print(f"  Users returned: {len(response['users'])}")
        else:
            print(f"Error: {response.get('error')}")
    
    print("\n" + "=" * 60)
    print("Mini Project Completed!")
    print("=" * 60)
    
    return api_lambda_handler


def run_all_exercises():
    """Run all Lambda-focused exercises."""
    print("=" * 70)
    print("AWS Lambda Python Exercises - Day 1")
    print("Focused on Lambda-specific patterns and best practices")
    print("=" * 70)
    
    print("\nThese exercises simulate Lambda development patterns.")
    print("Run them locally to understand concepts before deploying to AWS.\n")
    
    # Run exercises
    handler1 = exercise_1_lambda_handler_pattern()
    handler2 = exercise_2_environment_variables()
    handler3 = exercise_3_error_handling()
    handler4 = exercise_4_logging_and_monitoring()
    
    # Run mini project
    api_handler = mini_project_simple_api_lambda()
    
    print("\n" + "=" * 70)
    print("Summary of Concepts Learned:")
    print("=" * 70)
    print("1. ✅ Lambda handler pattern (event, context parameters)")
    print("2. ✅ Environment variable usage in Lambda")
    print("3. ✅ Comprehensive error handling for serverless")
    print("4. ✅ Structured logging for CloudWatch monitoring")
    print("5. ✅ API Gateway integration patterns")
    print("6. ✅ Best practices for production Lambda functions")
    
    print("\n" + "=" * 70)
    print("Next Steps for Bo:")
    print("=" * 70)
    print("1. Set up AWS account and configure CLI")
    print("2. Deploy a simple Lambda via AWS Console")
    print("3. Modify the API handler from mini project")
    print("4. Add tests for your Lambda functions")
    print("5. Explore AWS SAM for local development")
    
    print("\nGreat work! You've completed Day 1 of AWS Lambda Python training.")
    print("Remember: Practice deploying to AWS regularly, not just running locally.")
    
    return {
        'basic_handler': handler1,
        'env_handler': handler2,
        'error_handler': handler3,
        'logging_handler': handler4,
        'api_handler': api_handler
    }


if __name__ == "__main__":
    run_all_exercises()