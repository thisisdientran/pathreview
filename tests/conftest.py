"""Shared test fixtures for PathReview."""

from datetime import UTC, datetime

import pytest

from core.models.profile import Profile


@pytest.fixture
def sample_user_profile(sample_resume_text: str) -> Profile:
    """Return a realistic, persisted-looking user profile for testing."""
    created_at = datetime(2024, 1, 15, 12, 0, tzinfo=UTC)

    return Profile(
        id="123e4567-e89b-12d3-a456-426614174000",
        user_id="123e4567-e89b-12d3-a456-426614174001",
        github_username="janedoe",
        resume_filename="jane_doe_resume.pdf",
        resume_text=sample_resume_text,
        portfolio_url="https://janedoe.dev",
        created_at=created_at,
        updated_at=created_at,
    )


@pytest.fixture
def sample_resume_text() -> str:
    """Return a sample resume text for testing."""
    return """
    Jane Doe
    Software Engineer
    jane.doe@example.com | github.com/janedoe

    Experience:
    - Software Engineer at TechCorp (2022-2024)
      Built REST APIs using Python and FastAPI.

    Education:
    - B.S. Computer Science, State University (2022)

    Skills: Python, JavaScript, React, PostgreSQL, Docker
    """


@pytest.fixture
def sample_readme_text() -> str:
    """Return a sample README text for testing."""
    return """
    # Weather App
    A weather forecasting application built with React and OpenWeatherMap API.

    ## Features
    - Current weather display
    - 5-day forecast
    - Location search

    ## Tech Stack
    - React 18
    - TypeScript
    - Tailwind CSS
    - OpenWeatherMap API
    """
