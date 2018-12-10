from typing import List, Dict


DESCRIPTION = "description"
LANGUAGE = "language"
ACTIVE_ASSISTANT_AGENTS = "activeAssistantAgents"
DISABLE_INTERACTION_LOGS = "disableInteractionLogs"
DISABLE_STACKDRIVER_LOGS = "disableStackdriverLogs"
GOOGLE_ASSISTANT = "googleAssistant"
GOOGLE_ASSISTANT_GOOGLE_ASSISTANT_COMPATIBLE = "googleAssistantCompatible"
GOOGLE_ASSISTANT_PROJECT = "project"
GOOGLE_ASSISTANT_WELCOME_INTENT_SIGN_IN_REQUIRED = "welcomeIntentSignInRequired"
GOOGLE_ASSISTANT_START_INTENTS = "startIntents"
GOOGLE_ASSISTANT_SYSTEM_INTENTS = "systemIntents"
GOOGLE_ASSISTANT_END_INTENT_IDS = "endIntentIds"
GOOGLE_ASSISTANT_OAUTH_LINKING = "oAuthLinking"
GOOGLE_ASSISTANT_OAUTH_LINKING_REQUIRED = "required"
GOOGLE_ASSISTANT_OAUTH_LINKING_GRANT_TYPE = "grantType"
GOOGLE_ASSISTANT_VOICE_TYPE = "voiceType"
GOOGLE_ASSISTANT_CAPABILITIES = "capabilities"
GOOGLE_ASSISTANT_PROTOCOL_VERSION = "protocolVersion"
GOOGLE_ASSISTANT_IS_DEVICE_AGENT = "isDeviceAgent"
DEFAULT_TIMEZONE = "defaultTimezone"
WEBHOOK = "webhook"
WEBHOOK_URL = "url"
WEBHOOK_USERNAME = "username"
WEBHOOK_HEADERS = "headers"
WEBHOOK_AVAILABLE = "available"
WEBHOOK_USE_FOR_DOMAINS = "useForDomains"
WEBHOOK_CLOUD_FUNCTIONS_ENABLED = "cloudFunctionsEnabled"
WEBHOOK_CLOUD_FUNCTIONS_INITIALIZED = "cloudFunctionsInitialized"
IS_PRIVATE = "isPrivate"
CUSTOM_CLASSIFIER_MODE = "customClassifierMode"
ML_MIN_CONFIDENCE = "mlMinConfidence"
SUPPORTED_LANGUAGES = "supportedLanguages"
ONE_PLATFORM_API_VERSION = "onePlatformApiVersion"
ANALYZE_QUERY_TEXT_SENTIMENT = "analyzeQueryTextSentiment"
ENABLED_KNOWLEDGE_BASE_NAMES = "enabledKnowledgeBaseNames"
KNOWLEDGE_SERVICE_CONFIDENCE_ADJUSTMENT = "knowledgeServiceConfidenceAdjustment"
DIALOG_BUILDER_MODE = "dialogBuilderMode"

fields= [
DESCRIPTION,
LANGUAGE,
ACTIVE_ASSISTANT_AGENTS,

]

types = {
    DESCRIPTION: str,
    LANGUAGE: str,
    ACTIVE_ASSISTANT_AGENTS: List,
    DISABLE_INTERACTION_LOGS: bool
}

default = {
    DESCRIPTION: "",
    LANGUAGE: "en",
    ACTIVE_ASSISTANT_AGENTS: [],
    DISABLE_INTERACTION_LOGS: False
}
