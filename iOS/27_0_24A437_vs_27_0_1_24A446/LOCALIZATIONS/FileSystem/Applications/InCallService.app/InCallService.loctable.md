## InCallService

> `FileSystem/Applications/InCallService.app/InCallService.loctable`

```diff

 en.UNKNOWN_NUMBER_ALERT_MESSAGE = "This number is not in your contact list. If you don’t recognize the caller, it may be spam."
 en.UNKNOWN_NUMBER_ALERT_MESSAGE_WITH_LOCATION_%@ = "The country code for this number is %@. If you don’t recognize the caller, it may be spam."
 en.UNKNOWN_NUMBER_ALERT_TITLE_%@ = "Call %@?"
-en.UNSAFE_CALL_MESSAGE_%@ = "This link was blocked because it contains malware that will forward all of your incoming messages and calls to %@. Scammers often provide malicious links that look legitimate via email, text, or chat."
-en.UNSAFE_CALL_TITLE = "Malicious Link Blocked"
+en.UNSAFE_CALL_MESSAGE_%@ = "This link was blocked because it will forward all of your incoming messages and calls to %@. Scammers often provide malicious links that look legitimate via email, text, or chat to gain access to your data or device."
+en.UNSAFE_CALL_TITLE = "Call Forwarding Link Blocked"
 en.USE_CELLULAR_%@ = "Use Cellular to Call “%@”?"
 en.VIDEO = "Video"
 en.VIDEO_DEGRADED_MESSAGE = "The video will resume automatically when the connection improves."

```
