"""
AWS Bedrock Basics for Lambda Integration

This file demonstrates basic AWS Bedrock usage patterns that you'll need
for your Lambda functions. We'll simulate Bedrock calls since actual
Bedrock access requires AWS account setup and permissions.

Note: To run real Bedrock calls, you'll need:
1. AWS account with Bedrock access enabled
2. IAM permissions for Bedrock
3. boto3 configured with credentials
"""

import json
from typing import Dict, Any, List
import boto3  # Will fail without AWS config - that's OK for learning


class MockBedrockClient:
    """
    Mock Bedrock client for learning purposes.
    In real code, you'd use: boto3.client('bedrock-runtime')
    """
    
    @staticmethod
    def invoke_model(model_id: str, body: Dict) -> Dict:
        """
        Simulate Bedrock model invocation.
        
        Args:
            model_id: Bedrock model ID (e.g., 'anthropic.claude-v2')
            body: Request body with prompt and parameters
        
        Returns:
            Mock response similar to Bedrock's response
        """
        prompt = body.get('prompt', '')
        max_tokens = body.get('max_tokens_to_sample', 100)
        
        # Mock different model behaviors
        if 'claude' in model_id.lower():
            return MockBedrockClient._mock_claude_response(prompt, max_tokens)
        elif 'titan' in model_id.lower():
            return MockBedrockClient._mock_titan_response(prompt, max_tokens)
        elif 'llama' in model_id.lower():
            return MockBedrockClient._mock_llama_response(prompt, max_tokens)
        else:
            return MockBedrockClient._mock_generic_response(prompt, max_tokens)
    
    @staticmethod
    def _mock_claude_response(prompt: str, max_tokens: int) -> Dict:
        """Mock Anthropic Claude response."""
        responses = [
            f"Hello! I'm Claude, an AI assistant created by Anthropic. You asked: '{prompt}'",
            f"I understand you're asking about '{prompt}'. As an AI, I can help with...",
            f"Based on your prompt '{prompt}', here's what I think...",
            f"Thank you for your question about '{prompt}'. Let me provide some insights..."
        ]
        
        import hashlib
        hash_val = int(hashlib.md5(prompt.encode()).hexdigest(), 16)
        response_index = hash_val % len(responses)
        
        return {
            'completion': responses[response_index],
            'stop_reason': 'stop_sequence',
            'stop': '\n\nHuman:'
        }
    
    @staticmethod
    def _mock_titan_response(prompt: str, max_tokens: int) -> Dict:
        """Mock Amazon Titan response."""
        return {
            'results': [{
                'outputText': f"[Amazon Titan] Processing your request: '{prompt}'. " +
                             "This is a mock response since we're not actually calling Bedrock.",
                'completionReason': 'FINISH'
            }]
        }
    
    @staticmethod
    def _mock_llama_response(prompt: str, max_tokens: int) -> Dict:
        """Mock Meta Llama response."""
        return {
            'generation': f"[Llama 2] Your input: '{prompt}'. " +
                         "In a real Bedrock call, I would analyze this and provide a helpful response.",
            'stop_reason': 'length'
        }
    
    @staticmethod
    def _mock_generic_response(prompt: str, max_tokens: int) -> Dict:
        """Mock generic model response."""
        return {
            'text': f"Mock Bedrock response to: '{prompt}'. " +
                   f"This would use {max_tokens} tokens in a real call."
        }


def exercise_1_bedrock_basic_invocation():
    """
    Learn the basic pattern for invoking Bedrock models from Lambda.
    
    Real pattern:
    1. Create boto3 client for bedrock-runtime
    2. Prepare request body (model-specific format)
    3. Invoke the model
    4. Parse the response
    """
    
    print("Exercise 1: Basic Bedrock Invocation Pattern")
    print("=" * 60)
    
    # This is what real code would look like (commented since we need AWS setup)
    """
    # REAL CODE PATTERN (requires AWS setup):
    import boto3
    import json
    
    def invoke_bedrock_model(prompt: str, model_id: str = "anthropic.claude-v2") -> str:
        # Create Bedrock client
        client = boto3.client('bedrock-runtime', region_name='us-east-1')
        
        # Prepare request body (Claude format example)
        body = {
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens_to_sample": 300,
            "temperature": 0.5,
            "top_p": 0.9,
            "stop_sequences": ["\n\nHuman:"]
        }
        
        # Invoke model
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(body).encode('utf-8'),
            contentType='application/json',
            accept='application/json'
        )
        
        # Parse response
        response_body = json.loads(response['body'].read())
        return response_body['completion']
    """
    
    # Mock implementation for learning
    def mock_invoke_bedrock_model(prompt: str, model_id: str = "anthropic.claude-v2") -> str:
        """Mock version for learning the pattern."""
        
        # Step 1: Prepare request body (model-specific)
        if 'claude' in model_id:
            body = {
                "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
                "max_tokens_to_sample": 300,
                "temperature": 0.5,
                "top_p": 0.9,
                "stop_sequences": ["\n\nHuman:"]
            }
        elif 'titan' in model_id:
            body = {
                "inputText": prompt,
                "textGenerationConfig": {
                    "maxTokenCount": 300,
                    "temperature": 0.5,
                    "topP": 0.9
                }
            }
        else:
            body = {"prompt": prompt, "max_tokens": 300}
        
        print(f"Step 1: Prepared request body for {model_id}")
        print(f"       Prompt: '{prompt}'")
        print(f"       Body keys: {list(body.keys())}")
        
        # Step 2: Invoke model (mock)
        print("\nStep 2: Invoking model (mock)...")
        response = MockBedrockClient.invoke_model(model_id, body)
        
        # Step 3: Parse response
        print("\nStep 3: Parsing response...")
        
        if 'claude' in model_id:
            completion = response.get('completion', '')
        elif 'titan' in model_id:
            completion = response.get('results', [{}])[0].get('outputText', '')
        elif 'llama' in model_id:
            completion = response.get('generation', '')
        else:
            completion = response.get('text', '')
        
        print(f"       Extracted completion: {completion[:100]}...")
        
        return completion
    
    # Test the pattern
    test_prompts = [
        "Explain AWS Lambda in simple terms",
        "What is AWS Bedrock?",
        "How do I deploy a Python Lambda function?"
    ]
    
    test_models = [
        "anthropic.claude-v2",
        "amazon.titan-text-express-v1",
        "meta.llama2-13b-chat-v1"
    ]
    
    for i, (prompt, model_id) in enumerate(zip(test_prompts, test_models), 1):
        print(f"\n{'─' * 50}")
        print(f"Test {i}: Model={model_id}")
        print(f"Prompt: '{prompt}'")
        
        result = mock_invoke_bedrock_model(prompt, model_id)
        print(f"\nResult: {result[:150]}...")
    
    return mock_invoke_bedrock_model


def exercise_2_bedrock_in_lambda():
    """
    Learn how to integrate Bedrock into a Lambda function.
    
    Key considerations:
    1. IAM permissions (bedrock:InvokeModel)
    2. Cold start optimization
    3. Error handling
    4. Response formatting
    """
    
    print("\n\nExercise 2: Bedrock in Lambda Function")
    print("=" * 60)
    
    def lambda_handler_with_bedrock(event, context):
        """
        Lambda handler that uses Bedrock for AI capabilities.
        
        Expected event format (API Gateway):
        {
          "httpMethod": "POST",
          "path": "/ask",
          "body": "{\"question\": \"What is serverless?\"}"
        }
        """
        import json
        import os
        
        print("Lambda execution started")
        
        try:
            # Parse request
            if event.get('body'):
                request_data = json.loads(event['body'])
                question = request_data.get('question', '')
            else:
                question = event.get('question', '')
            
            if not question:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'No question provided'})
                }
            
            print(f"Processing question: {question[:50]}...")
            
            # Get configuration from environment variables
            model_id = os.environ.get('BEDROCK_MODEL', 'anthropic.claude-v2')
            max_tokens = int(os.environ.get('MAX_TOKENS', '300'))
            
            # In real code: Initialize Bedrock client outside handler for cold start optimization
            # client = boto3.client('bedrock-runtime')  # Real initialization
            
            # Mock Bedrock call
            print(f"Calling Bedrock model: {model_id}")
            
            # Prepare request (mock)
            body = {
                "prompt": f"\n\nHuman: {question}\n\nAssistant:",
                "max_tokens_to_sample": max_tokens,
                "temperature": 0.7
            }
            
            # Mock invocation
            mock_response = MockBedrockClient.invoke_model(model_id, body)
            answer = mock_response.get('completion', 'No response generated')
            
            # Format response
            response_data = {
                'question': question,
                'answer': answer,
                'model': model_id,
                'tokens_used': len(answer.split()),  # Mock token count
                'timestamp': '2024-01-01T00:00:00Z'  # In real code: datetime.utcnow().isoformat()
            }
            
            print("Successfully generated response")
            
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'X-Model-Used': model_id
                },
                'body': json.dumps(response_data)
            }
            
        except json.JSONDecodeError:
            print("Error: Invalid JSON in request")
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid JSON in request body'})
            }
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'Internal server error'})
            }
    
    # Test the Lambda handler
    print("Testing Lambda handler with Bedrock integration...")
    
    test_cases = [
        {
            'name': 'Valid question via API Gateway',
            'event': {
                'httpMethod': 'POST',
                'path': '/ask',
                'body': json.dumps({'question': 'What is AWS Lambda?'})
            },
            'env_vars': {'BEDROCK_MODEL': 'anthropic.claude-v2'}
        },
        {
            'name': 'Direct invocation',
            'event': {'question': 'Explain Bedrock models'},
            'env_vars': {'BEDROCK_MODEL': 'amazon.titan-text-express-v1'}
        },
        {
            'name': 'Empty question',
            'event': {'body': json.dumps({'question': ''})},
            'env_vars': {}
        },
        {
            'name': 'Invalid JSON',
            'event': {'body': '{invalid json}'},
            'env_vars': {}
        }
    ]
    
    # Mock environment variables
    import os
    original_env = os.environ.copy()
    
    try:
        for test in test_cases:
            print(f"\n{'─' * 50}")
            print(f"Test: {test['name']}")
            
            # Set environment variables
            os.environ.update(test['env_vars'])
            
            result = lambda_handler_with_bedrock(test['event'], None)
            response = json.loads(result['body']) if result['body'] else {}
            
            print(f"Status Code: {result['statusCode']}")
            
            if result['statusCode'] == 200:
                print(f"Success! Model: {response.get('model')}")
                print(f"Answer preview: {response.get('answer', '')[:100]}...")
            else:
                print(f"Error: {response.get('error')}")
                
    finally:
        # Restore environment
        os.environ.clear()
        os.environ.update(original_env)
    
    return lambda_handler_with_bedrock


def exercise_3_bedrock_error_handling():
    """
    Learn error handling patterns for Bedrock calls in Lambda.
    
    Common errors:
    1. Model not available in region
    2. Rate limiting
    3. Invalid request format
    4. Permission issues
    """
    
    print("\n\nExercise 3: Bedrock Error Handling")
    print("=" * 60)
    
    class BedrockError(Exception):
        """Base exception for Bedrock-related errors."""
        pass
    
    class ModelNotAvailableError(BedrockError):
        """Raised when requested model is not available."""
        pass
    
    class RateLimitError(BedrockError):
        """Raised when rate limit is exceeded."""
        pass
    
    class InvalidRequestError(BedrockError):
        """Raised when request is malformed."""
        pass
    
    def safe_bedrock_invocation(prompt: str, model_id: str, max_retries: int = 3) -> Dict:
        """
        Safely invoke Bedrock with error handling and retries.
        
        Args:
            prompt: User prompt
            model_id: Bedrock model ID
            max_retries: Maximum retry attempts
        
        Returns:
            Response dict or raises appropriate error
        """
        # In real code, this would use boto3
        # For learning, we'll simulate different error scenarios
        
        import random
        import time
        
        # Simulate different failure scenarios
        scenario = random.choice(['success', 'rate_limit', 'model_unavailable', 'invalid_request'])
        
        print(f"  Attempting Bedrock invocation...")
        print(f"  Model: {model_id}, Prompt: '{prompt[:30]}...'")
        print(f"  Simulated scenario: {scenario}")
        
        if scenario == 'success':
            # Successful invocation
            return MockBedrockClient.invoke_model(model_id, {'prompt': prompt})
        
        elif scenario == 'rate_limit':
            raise RateLimitError(f"Rate limit exceeded for model {model_id}. Try again later.")
        
        elif scenario == 'model_unavailable':
            raise ModelNotAvailableError(
                f"Model {model_id} is not available in this region. "
                f"Available models: anthropic.claude-v2, amazon.titan-text-express-v1"
            )
        
        elif scenario == 'invalid_request':
            raise InvalidRequestError(
                f"Invalid request format for model {model_id}. "
                f"Check prompt length and parameters."
            )
    
    def resilient_lambda_handler(event, context):
        """
        Lambda handler with resilient Bedrock integration.
        """
        import json
        
        try:
            # Parse input
            question = event.get('question', '')
            if not question:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'No question provided'})
                }
            
            # Configuration
            model_id = 'anthropic.claude-v2'
            max_retries = 2
            
            # Attempt Bedrock invocation with retries
            last_error = None
            
            for attempt in range(max_retries + 1):
                try:
                    print(f"Attempt {attempt + 1} of {max_retries + 1}")
                    
                    response = safe_bedrock_invocation(question, model_id)
                    answer = response.get('completion', '')
                    
                    # Success!
                    return {
                        'statusCode': 200,
                        'body': json.dumps({
                            'question': question,
                            'answer': answer,
                            'attempts': attempt + 1
                        })
                    }
                    
                except RateLimitError as e:
                    last_error = e
                    print(f"Rate limit error: {e}")
                    
                    if attempt < max_retries:
                        # Exponential backoff
                        wait_time = (2 ** attempt) * 0.1  # 0.1s, 0.2s, 0.4s
                        print(f"  Waiting {wait_time}s before retry...")
                        time.sleep(wait_time)
                    continue
                    
                except ModelNotAvailableError as e:
                    last_error = e
                    print(f"Model unavailable: {e}")
                    # No retry for this error - try different model
                    model_id = 'amazon.titan-text-express-v1'  # Fallback model
                    continue
                    
                except InvalidRequestError as e:
                    last_error = e
                    print(f"Invalid request: {e}")
                    # Fix the request
                    if len(question) > 1000:
                        question = question[:1000] + "...[truncated]"
                        continue
                    else:
                        # Can't fix this type of error
                        break
                        
                except Exception as e:
                    last_error = e
                    print(f"Unexpected error: {e}")
                    break
            
            # If we get here, all attempts failed
            error_message = str(last_error) if last_error else "Unknown error"
            
            return {
                'statusCode': 503,
                'body': json.dumps({
                    'error': 'Failed to generate response',
                    'details': error_message,
                    'suggestion': 'Please try again later or rephrase your question'
                })
            }
            
        except Exception as e:
            print(f"Lambda handler error: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'Internal server error'})
            }
    
    # Test error handling
    print("Testing resilient Bedrock integration...")
    
    # We'll run multiple times to see different scenarios
    for i in range(5):
        print(f"\nTest run {i + 1}:")
        result = resilient_lambda_handler(
            {'question': 'What is AWS Bedrock and how does it work?'},
            None
        )
        
        response = json.loads(result['body'])
        
        if result['statusCode'] == 200:
            print(f"  ✅ Success after {response.get('attempts', 1)} attempts")
            print(f"  Answer preview: {response.get('answer', '')[:80]}...")
        else:
            print(f"  ❌ Failed with status {result['statusCode']}")
            print(f"  Error: {response.get('error')}")
            print(f"  Details: {response.get('details', 'None')}")
    
    return resilient_lambda_handler


def mini_project_ai_chatbot_lambda():
    """
    Mini Project: Build an AI chatbot Lambda using Bedrock patterns.
    
    This simulates a real-world Lambda that:
    1. Accepts chat messages
    2. Maintains conversation context
    3. Uses Bedrock for responses
    4. Handles errors gracefully
    """
    
    print("\n" + "=" * 70)
    print("Mini Project: AI Chatbot Lambda with Bedrock")
    print("=" * 70)
    
    class ChatbotMemory:
        """Simple in-memory conversation memory."""
        
        def __init__(self, max_messages: int = 10):
            self.conversations = {}
            self.max_messages = max_messages
        
        def get_conversation(self, session_id: str) -> List[Dict]:
            """Get conversation history for a session."""
            return self.conversations.get(session_id, [])
        
        def add_message(self, session_id: str, role: str, content: str):
            """Add a message to conversation history."""
            if session_id not in self.conversations:
                self.conversations[session_id] = []
            
            self.conversations[session_id].append({
                'role': role,
                'content': content,
                'timestamp': '2024-01-01T00:00:00Z'  # Mock timestamp
            })
            
            # Keep only recent messages
            if len(self.conversations[session_id]) > self.max_messages:
                self.conversations[session_id] = self.conversations[session_id][-self.max_messages:]
    
    def build_conversation_prompt(messages: List[Dict]) -> str:
        """Build a prompt from conversation history."""
        prompt_parts = []
        
        for msg in messages[-5:]:  # Last 5 messages for context
            if msg['role'] == 'user':
                prompt_parts.append(f"\n\nHuman: {msg['content']}")
            elif msg['role'] == 'assistant':
                prompt_parts.append(f"\n\nAssistant: {msg['content']}")
        
        # Add current turn
        prompt_parts.append("\n\nAssistant:")
        
        return ''.join(prompt_parts)
    
    def ai_chatbot_lambda(event, context):
        """
        AI Chatbot Lambda handler.
        
        Expected event:
        {
          "sessionId": "user-123",
          "message": "Hello, how are you?",
          "resetConversation": false  // Optional
        }
        """
        import json
        
        print("Chatbot Lambda invoked")
        
        try:
            # Parse request
            session_id = event.get('sessionId', 'default-session')
            user_message = event.get('message', '')
            reset_conversation = event.get('resetConversation', False)
            
            if not user_message:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'No message provided'})
                }
            
            # Initialize memory (in real Lambda, use DynamoDB)
            memory = ChatbotMemory()
            
            # Reset conversation if requested
            if reset_conversation:
                memory.conversations.pop(session_id, None)
            
            # Add user message to memory
            memory.add_message(session_id, 'user', user_message)
            
            # Get conversation history
            conversation = memory.get_conversation(session_id)
            
            # Build prompt from conversation
            prompt = build_conversation_prompt(conversation)
            print(f"Built prompt with {len(conversation)} messages")
            
            # Call Bedrock (mock)
            model_id = 'anthropic.claude-v2'
            body = {
                'prompt': prompt,
                'max_tokens_to_sample': 500,
                'temperature': 0.7,
                'top_p': 0.9
            }
            
            print(f"Calling Bedrock model: {model_id}")
            response = MockBedrockClient.invoke_model(model_id, body)
            ai_response = response.get('completion', "I'm sorry, I couldn't generate a response.")
            
            # Add AI response to memory
            memory.add_message(session_id, 'assistant', ai_response)
            
            # Return response
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'response': ai_response,
                    'sessionId': session_id,
                    'messageCount': len(memory.get_conversation(session_id)),
                    'modelUsed': model_id
                })
            }
            
        except Exception as e:
            print(f"Chatbot error: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'error': 'Chatbot service unavailable',
                    'message': 'Please try again later'
                })
            }
    
    # Test the chatbot
    print("\nTesting AI Chatbot Lambda...")
    print("Simulating a conversation with the chatbot:\n")
    
    test_conversation = [
        {"sessionId": "test-user-1", "message": "Hello, who are you?"},
        {"sessionId": "test-user-1", "message": "What can you help me with?"},
        {"sessionId": "test-user-1", "message": "Tell me about AWS Lambda"},
        {"sessionId": "test-user-2", "message": "Hi, new conversation please", "resetConversation": True},
        {"sessionId": "test-user-2", "message": "What is Bedrock?"}
    ]
    
    for i, message in enumerate(test_conversation, 1):
        print(f"Turn {i}: User says: '{message['message']}'")
        
        result = ai_chatbot_lambda(message, None)
        response = json.loads(result['body'])
        
        if result['statusCode'] == 200:
            print(f"  🤖 Bot: {response['response'][:80]}...")
            print(f"  Session: {response['sessionId']}, Messages: {response['messageCount']}")
        else:
            print(f"  ❌ Error: {response.get('error')}")
        
        print()
    
    print("\n" + "=" * 70)
    print("Mini Project Completed!")
    print("=" * 70)
    
    return ai_chatbot_lambda


def run_all_bedrock_exercises():
    """Run all Bedrock-focused exercises."""
    print("=" * 70)
    print("AWS Bedrock & Lambda Integration Exercises")
    print("Patterns and best practices for AI-enabled serverless applications")
    print("=" * 70)
    
    print("\nNote: These exercises use mock Bedrock clients.")
    print("To run real Bedrock calls, you need:")
    print("1. AWS account with Bedrock access enabled")
    print("2. IAM permissions for bedrock:InvokeModel")
    print("3. boto3 configured with AWS credentials\n")
    
    # Run exercises
    print("Starting exercises...\n")
    
    bedrock_invoker = exercise_1_bedrock_basic_invocation()
    lambda_handler = exercise_2_bedrock_in_lambda()
    error_handler = exercise_3_bedrock_error_handling()
    chatbot = mini_project_ai_chatbot_lambda()
    
    print("\n" + "=" * 70)
    print("Summary of Bedrock Concepts Learned:")
    print("=" * 70)
    print("1. ✅ Bedrock invocation patterns (different model formats)")
    print("2. ✅ Integrating Bedrock into Lambda functions")
    print("3. ✅ Error handling and retry logic for AI services")
    print("4. ✅ Building conversational AI with memory/context")
    print("5. ✅ Best practices for production AI applications")
    
    print("\n" + "=" * 70)
    print("Next Steps for Bo's Bedrock Learning:")
    print("=" * 70)
    print("1. ✅ Understand the patterns (done!)")
    print("2. 🔄 Set up AWS account with Bedrock access")
    print("3. 🔄 Request model access (Claude, Titan, Llama)")
    print("4. 🔄 Update exercises to use real boto3 calls")
    print("5. 🔄 Deploy AI-enabled Lambda to AWS")
    print("6. 🔄 Monitor costs and usage")
    
    print("\nKey AWS Services to Learn:")
    print("- AWS Bedrock (Foundation models)")
    print("- AWS Lambda (Execution)")
    print("- API Gateway (REST API frontend)")
    print("- DynamoDB (Conversation storage)")
    print("- CloudWatch (Monitoring & logs)")
    
    print("\nRemember: Start with mock implementations, then")
    print("replace with real AWS calls as you get access.")
    print("\nGreat work! You're building the foundation for")
    print("AI-powered serverless applications. 🚀")
    
    return {
        'bedrock_invoker': bedrock_invoker,
        'lambda_handler': lambda_handler,
        'error_handler': error_handler,
        'chatbot': chatbot
    }


if __name__ == "__main__":
    run_all_bedrock_exercises()