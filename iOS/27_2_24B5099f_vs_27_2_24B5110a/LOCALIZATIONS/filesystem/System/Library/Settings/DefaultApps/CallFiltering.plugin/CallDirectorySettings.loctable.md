## CallFiltering

> `FileSystem/System/Library/Settings/DefaultApps/CallFiltering.plugin/CallDirectorySettings.loctable`

```diff

 en.OK = "OK"
 en.SPAM_SIMS_EXTENSIONS_LIST_FOOTER_%@ = "Calls identified as spam or fraud by %@ will be silenced, sent to voicemail, and moved to the Spam list."
 en.SPAM_SIMS_EXTENSIONS_LIST_FOOTER_%@_%@_DS_BOTH = "Calls identified as spam or fraud by %1$@ and %2$@ will be silenced, sent to voicemail, and moved to the Spam list."
+en.SPAM_SIMS_EXTENSIONS_LIST_FOOTER_%@_%@_DS_BOTH_ARBITRATION_ENABLED = "Callers identified as spam or fraud by %1$@ and %2$@ are silenced and moved to the Spam list. Voicemails identified by Apple are also moved to the Spam list."
 en.SPAM_SIMS_EXTENSIONS_LIST_FOOTER_%@_%@_DS_SINGLE = "Calls identified as spam or fraud by %@ will be silenced, sent to voicemail, and moved to the Spam list. Only incoming calls to numbers on your %@ plan will be blocked."
+en.SPAM_SIMS_EXTENSIONS_LIST_FOOTER_%@_%@_DS_SINGLE_ARBITRATION_ENABLED = "Callers identified as spam or fraud by %@ are silenced and moved to the Spam list. Only incoming calls to numbers on your %@ plan will be blocked. Voicemails identified by Apple are also moved to the Spam list."
+en.SPAM_SIMS_EXTENSIONS_LIST_FOOTER_%@_ARBITRATION_ENABLED = "Callers identified as spam or fraud by %@ are silenced and moved to the Spam list. Voicemails identified by Apple are also moved to the Spam list."
 en.SPAM_SIMS_EXTENSIONS_MORE_INFORMATION_%@ = "More about junk call silencing on %@"
 en.SPAM_SIMS_LIST_HEADER = "Carrier Call Identification"
+en.SPAM_TOGGLE_FOOTER_APPLE_ONLY = "Voicemails identified as spam or fraud by Apple are moved to the Spam list."
 en.SPAM_TOGGLE_TITLE = "Spam"

```
