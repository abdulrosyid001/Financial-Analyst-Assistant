import dspy
from transformers import AutoModelForCausalLM, AutoTokenizer
from ..utils.config import MODEL_NAME, DEVICE

# Load the model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map=DEVICE, torch_dtype="auto")

# DSPy LM
lm = dspy.HFModel(model=model, tokenizer=tokenizer)

# Set DSPy settings
dspy.settings.configure(lm=lm)

# Signatures
class MarketAnalysis(dspy.Signature):
    """Analyze market conditions based on provided data."""
    market_data: str = dspy.InputField()
    analysis: str = dspy.OutputField(desc="Summary of market conditions")

class PortfolioRisk(dspy.Signature):
    """Explain portfolio risk based on analytics."""
    analytics: str = dspy.InputField()
    risk_explanation: str = dspy.OutputField(desc="Explanation of portfolio risk")

class InvestmentRecommendation(dspy.Signature):
    """Provide investment recommendations."""
    portfolio_data: str = dspy.InputField()
    recommendation: str = dspy.OutputField(desc="Investment advice")

# Modules
market_analyzer = dspy.ChainOfThought(MarketAnalysis)
risk_explainer = dspy.ChainOfThought(PortfolioRisk)
recommender = dspy.ChainOfThought(InvestmentRecommendation)

def analyze_market(market_data: str) -> str:
    result = market_analyzer(market_data=market_data)
    return result.analysis

def explain_risk(analytics: str) -> str:
    result = risk_explainer(analytics=analytics)
    return result.risk_explanation

def recommend_investment(portfolio_data: str) -> str:
    result = recommender(portfolio_data=portfolio_data)
    return result.recommendation