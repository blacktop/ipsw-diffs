## maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

-3826.200.67.0.0
-  __TEXT.__text: 0xbccf4
+3826.200.84.0.0
+  __TEXT.__text: 0xbd32c
   __TEXT.__auth_stubs: 0x1210
-  __TEXT.__objc_stubs: 0x16080
-  __TEXT.__objc_methlist: 0x93e4
-  __TEXT.__gcc_except_tab: 0x1aa0c
-  __TEXT.__objc_methname: 0x1bcb2
-  __TEXT.__cstring: 0x8252
-  __TEXT.__objc_classname: 0x1b31
-  __TEXT.__objc_methtype: 0x3a9f
+  __TEXT.__objc_stubs: 0x16140
+  __TEXT.__objc_methlist: 0x9414
+  __TEXT.__gcc_except_tab: 0x1aad4
+  __TEXT.__objc_methname: 0x1bdc8
+  __TEXT.__cstring: 0x8341
+  __TEXT.__objc_classname: 0x1b45
+  __TEXT.__objc_methtype: 0x3a7f
   __TEXT.__const: 0x1d0
-  __TEXT.__oslogstring: 0x91d3
+  __TEXT.__oslogstring: 0x920e
   __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0x6810
+  __TEXT.__unwind_info: 0x6858
   __DATA_CONST.__auth_got: 0x918
   __DATA_CONST.__got: 0x11d0
-  __DATA_CONST.__const: 0x4858
-  __DATA_CONST.__cfstring: 0x6e20
+  __DATA_CONST.__const: 0x4898
+  __DATA_CONST.__cfstring: 0x6ec0
   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x2e8

   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x16370
-  __DATA.__objc_selrefs: 0x6938
-  __DATA.__objc_ivar: 0xc1c
+  __DATA.__objc_const: 0x163d8
+  __DATA.__objc_selrefs: 0x6968
+  __DATA.__objc_ivar: 0xc24
   __DATA.__objc_data: 0x36b0
   __DATA.__data: 0x2498
   __DATA.__bss: 0x764

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4055
+  Functions: 4063
   Symbols:   889
-  CStrings:  7314
+  CStrings:  7331
 
Symbols:
+ _EMUserDefaultNotificationPostingDelayTime
+ _MSUserNotificationCenterPostingDelay
+ _OBJC_CLASS_$_BGSystemTaskScheduler
- _OBJC_CLASS_$_EMNSUserDefaultsBoolObserver
- _EMUserDefaultDisableAutomaticMessageSummarization
- _OBJC_CLASS_$_MFMixedMessageFragment
CStrings:
+ "com.apple.mail.messageauthentication"
+ "_postingDelayFromDefaults"
+ "MFNanoServerMessageContentURLProtocol"
+ "summarizationSetting"
+ "getNotificationSettingsWithCompletionHandler:"
+ "_notificationSummarizationEnabled"
+ "_notificationPostingDelayToken"
+ "T@\"_MFNanoServerMessageContentURLProtocolRegistry\",&,N"
+ "v16@?0@\"UNNotificationSettings\"8"
+ "deregisterTaskWithIdentifier:"
+ "T@\"<EFCancelable>\",&,N,V_notificationPostingDelayToken"
+ "com.apple.email.searchIndexerBGTask"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "setNotificationPostingDelayToken:"
+ "sharedScheduler"
+ "loading message %!{(MISSING)public}@ had error %!{(MISSING)public}@"
+ "mf_markupString"
+ "notificationSummarizationEnabled"
+ "_setupPostingDelayDefaultsObserver"
+ "TB,R,N,V_notificationSummarizationEnabled"
+ "_updatePostingDelay:"
+ "com.apple.email.categorization.FastPass"
+ "v16@?0@\"BGSystemTask\"8"
+ "Generated summary updated for %!{(MISSING)public}@"
+ "com.apple.mail.blackpearl.categorizer"
+ "notificationPostingDelayToken"
+ "com.apple.email.search.FastPass"
+ "_MFNanoServerMessageContentURLProtocolRegistry"
+ "_summarizationSettingLock"
+ "Notification summarization enabled: %!{(MISSING)BOOL}d"
- "_automaticallySummarizeMessages"
- "T@\"_MFMessageContentURLProtocolRegistry\",&,N"
- "markupString"
- "setAutomaticallySummarizeMessages:"
- "MFMessageContentURLProtocol"
- "initWithUserDefaultKey:keyRepresentsDisabled:handler:"
- "_MFMessageContentURLProtocolRegistry"
- "mf_messageFragment"
- "@\"EMNSUserDefaultsBoolObserver\""
- "loading message %!{(MISSING)public}@ had error (%!{(MISSING)public}@/%!l(MISSING)d): fragment %!{(MISSING)public}@"
- "T@\"EMNSUserDefaultsBoolObserver\",&,N,V_automaticallySummarizeMessages"
- "initWithMarkupString:baseURL:"
- "automaticallySummarizeMessages"

```
