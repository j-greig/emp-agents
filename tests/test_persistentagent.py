import pytest

from emp_agents.agents.persistentagent import PersistentAgent, PersistentAgentConfig


@pytest.mark.asyncio(scope="session")
async def test_from_config():
    config = PersistentAgentConfig(
        agent_id="test-agent-1",
        name="Test Agent",
        description="A test agent",
        default_model="gpt-3.5-turbo",
        prompt="You are a test assistant",
        tools=[],
        requires=[],
    )
    agent = PersistentAgent.from_config(config)

    assert isinstance(agent, PersistentAgent)
    assert agent.config == config
    assert agent.description == config.description
    assert agent.default_model == config.default_model
    assert agent.prompt == config.prompt
    assert agent.tools == config.tools
    assert agent.requires == config.requires
    assert agent.personality == config.name


@pytest.mark.asyncio(scope="session")
async def test_perform_action(capsys):
    config = PersistentAgentConfig(
        agent_id="test-agent-1",
        name="Test Agent",
        description="A test agent",
        default_model="gpt-3.5-turbo",
        prompt="You are a test assistant",
        tools=[],
        requires=[],
    )
    agent = PersistentAgent.from_config(config)
    agent.perform_action()

    captured = capsys.readouterr()
    expected_output = (
        f"Agent {config.name} (ID: {config.agent_id}) is performing an action.\n"
    )
    assert captured.out == expected_output
