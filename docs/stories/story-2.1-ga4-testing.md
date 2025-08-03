# Story 2.1: GA4 MCP Integration Testing

## Story

As a Developer, I want to test the GA4 MCP integration, so that we can ensure that basic website traffic and conversion data is flowing into our system correctly.

## Acceptance Criteria

1. A test script is created to pull key data points (user acquisition, conversions, audience segments) from GA4 via the specified MCP.
2. The script successfully connects to the GA4 API in the sandbox environment.
3. The script can retrieve data for the last 7 days without errors.
4. The retrieved data is logged to a file or console for verification.
5. The test script is committed to the project's repository.

## QA Plan

- Review the test script for correctness.
- Execute the script and verify that the output log contains valid GA4 data.
- Ensure no sensitive credentials are hardcoded in the script.
