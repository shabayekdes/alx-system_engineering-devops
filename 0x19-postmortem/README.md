# 0x19. Postmortem

## Issue Summary:

### Duration:

Start Time: Feb 16, 2024, 02:00 AM (UTC)
End Time: Feb 16, 2024, 04:30 AM (UTC)

### Impact:

During the incident window, users were unable to receive OTPs for login authentication. This resulted in a complete halt of the login process, affecting 15% of our user base and causing frustration among affected users.

### Root Cause:

The root cause of the issue was identified as a misconfiguration in the third-party SMS gateway integration, leading to the failure of OTP delivery.

### Timeline:

- 2:00 PM: Issue detected through an increase in customer support inquiries related to OTP non-reception.

- 2:15 PM: Investigated potential issues with the OTP generation algorithm, as initial indicators suggested a problem in the backend OTP generation process.

- 2:45 PM: Misleading path - Focused on network connectivity, assuming a problem with the SMS gateway's connection, delaying the identification of the root cause.

- 3:30 PM: Escalated the incident to the integration team after recognizing the issue's impact on OTP delivery.

- 4:00 PM: Identified misconfiguration in the third-party SMS gateway integration, causing OTP delivery failures.

- 4:15 PM: Temporarily switched to an alternate SMS gateway to resume OTP delivery while working on a permanent fix.

- 4:30 PM: Implemented a configuration fix in the SMS gateway integration, ensuring successful OTP delivery to users.

## Root Cause and Resolution:

### Root Cause: 

A misconfiguration in the third-party SMS gateway integration led to the failure of OTP delivery, preventing users from receiving authentication codes.

### Resolution:

Temporarily switched to an alternate SMS gateway to restore OTP delivery while concurrently implementing a configuration fix in the original SMS gateway integration to prevent future occurrences.

## Corrective and Preventative Measures:

### Improvements/Fixes:

Implement automated tests for third-party integrations to detect misconfigurations in real-time.
Enhance monitoring for OTP delivery, specifically focusing on success rates and response times.
Establish a communication protocol with the third-party SMS gateway provider to streamline issue resolution in the future.
Tasks to Address the Issue:

Communicate the incident details and resolution to affected users.
Conduct a comprehensive review of third-party integrations to identify and rectify potential misconfigurations.
Schedule regular audits of third-party integration configurations to ensure ongoing system stability.

## Conclusion:

The backend login authentication issue on Feb 16, 2024, was attributed to a misconfiguration in the third-party SMS gateway integration, resulting in the failure of OTP delivery. Swift resolution was achieved by temporarily switching to an alternate SMS gateway while addressing the misconfiguration. The incident highlights the importance of proactive monitoring and automated testing for third-party integrations to ensure a seamless user experience. Ongoing measures, including regular audits and enhanced monitoring, have been implemented to prevent similar issues in the future.
