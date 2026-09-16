## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`

```diff

-3896.100.1.2.1
-  __TEXT.__text: 0x812c0
+3896.200.31.0.0
+  __TEXT.__text: 0x82618
   __TEXT.__auth_stubs: 0x11d0
   __TEXT.__lazy_helpers: 0xfc
-  __TEXT.__objc_stubs: 0xa940
-  __TEXT.__objc_methlist: 0x61bc
+  __TEXT.__objc_stubs: 0xab60
+  __TEXT.__objc_methlist: 0x6334
   __TEXT.__const: 0x270
-  __TEXT.__gcc_except_tab: 0xe5d4
-  __TEXT.__cstring: 0x3a89
-  __TEXT.__objc_methname: 0xf03c
-  __TEXT.__objc_classname: 0xb94
-  __TEXT.__objc_methtype: 0x2f57
-  __TEXT.__oslogstring: 0xf76e
-  __TEXT.__unwind_info: 0x30c8
-  __DATA_CONST.__const: 0x15c0
-  __DATA_CONST.__cfstring: 0x1dc0
-  __DATA_CONST.__objc_classlist: 0x238
+  __TEXT.__gcc_except_tab: 0xe820
+  __TEXT.__cstring: 0x3cc8
+  __TEXT.__objc_methname: 0xf534
+  __TEXT.__objc_classname: 0xbd1
+  __TEXT.__objc_methtype: 0x2f81
+  __TEXT.__oslogstring: 0xf8cf
+  __TEXT.__unwind_info: 0x3158
+  __DATA_CONST.__const: 0x15e8
+  __DATA_CONST.__cfstring: 0x1e00
+  __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x228

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x900
-  __DATA_CONST.__got: 0x7a0
+  __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x8cf8
-  __DATA.__objc_selrefs: 0x3718
-  __DATA.__objc_ivar: 0x6d0
-  __DATA.__objc_data: 0x1630
+  __DATA.__objc_const: 0x9000
+  __DATA.__objc_selrefs: 0x37d0
+  __DATA.__objc_ivar: 0x6f0
+  __DATA.__objc_data: 0x1680
   __DATA.__lazy_load_got: 0x18
-  __DATA.__data: 0xe4c
+  __DATA.__data: 0xeac
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2074
-  Symbols:   516
-  CStrings:  3843
+  Functions: 2102
+  Symbols:   518
+  CStrings:  3899
 
Symbols:
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_AVAssetDownloadLiveActivity
CStrings:
+ "\t"
+ "%{public}@ eligible for a Live Activity"
+ "%{public}@ no Live Activity: %{public}s"
+ "@\"NDAVBackgroundSession\""
+ "AVAssetDownloadFailOnRetryableError"
+ "AVAssetDownloadLiveActivityDownload"
+ "AVAssetDownloadTaskLiveActivityEnabledKey"
+ "CREATE INDEX IF NOT EXISTS idx_session_tasks_session_bundle ON session_tasks(session_id, bundle_id);"
+ "Cancelling task %lu because the user dismissed its Live Activity"
+ "Failed to bind session limit params to the insert statement"
+ "Failed to create session_tasks index"
+ "Failed to migrate to version 4"
+ "NDAVLiveActivityDownload"
+ "REPLACE INTO sessions (bundle_id, session_id, configuration, options) \tSELECT ?, ?, ?, (SELECT options FROM sessions WHERE bundle_id = ? AND session_id = ?) \tWHERE EXISTS (SELECT 1 FROM sessions WHERE bundle_id = ? AND session_id = ?) \t\tOR (SELECT COUNT(*) FROM sessions WHERE bundle_id = ?) < ?"
+ "REPLACE INTO sessions (bundle_id, session_id, options, configuration) \tSELECT ?, ?, ?, (SELECT configuration FROM sessions WHERE bundle_id = ? AND session_id = ?) \tWHERE EXISTS (SELECT 1 FROM sessions WHERE bundle_id = ? AND session_id = ?) \t\tOR (SELECT COUNT(*) FROM sessions WHERE bundle_id = ?) < ?"
+ "Refused to persist session %@ for bundle %{public}@: session limit (%d) reached"
+ "T@\"NDAVBackgroundSession\",W,N,V_session"
+ "T@\"NSString\",C,N,V_liveActivityAssetTitle"
+ "T@\"NSString\",C,N,V_liveActivityClientBundleIdentifier"
+ "T@\"NSString\",C,N,V_liveActivityDownloadIdentifier"
+ "T@\"NSString\",R,C,N"
+ "Tq,N,V_liveActivityBytesExpectedToWrite"
+ "Tq,N,V_liveActivityBytesWritten"
+ "Tq,R,N"
+ "_identifiersToLiveActivityDownloads"
+ "_liveActivityAssetTitle"
+ "_liveActivityBytesExpectedToWrite"
+ "_liveActivityBytesWritten"
+ "_liveActivityClientBundleIdentifier"
+ "_liveActivityDownloadIdentifier"
+ "discretionary at first resume"
+ "downloadDidEnterRetry:"
+ "isLiveActivityEligibleTaskInfo:"
+ "isLiveActivityEnabled"
+ "liveActivityAssetTitle"
+ "liveActivityBytesExpectedToWrite"
+ "liveActivityBytesWritten"
+ "liveActivityClientBundleIdentifier"
+ "liveActivityDownloadForTaskIdentifier:"
+ "liveActivityDownloadIdentifier"
+ "liveActivityRequestsCancellation"
+ "liveActivityRequestsCancellationOfTaskWithIdentifier:"
+ "liveActivityTerminalStatusForClientError:"
+ "notifyProgress:"
+ "opted out by download configuration"
+ "opted out by legacy option"
+ "registerDownload:"
+ "setLiveActivityAssetTitle:"
+ "setLiveActivityBytesExpectedToWrite:"
+ "setLiveActivityBytesWritten:"
+ "setLiveActivityClientBundleIdentifier:"
+ "setLiveActivityDownloadIdentifier:"
+ "startedUserInitiated not set"
+ "unregisterDownload:terminalStatus:error:"
+ "unregisterLiveActivityForTaskWithIdentifier:terminalStatus:error:"
+ "updateLiveActivityForResumedTaskWithIdentifier:"
+ "updateLiveActivityForRetryingTaskWithIdentifier:"
+ "updateWorkState"
+ "v40@0:8Q16q24@32"
- "REPLACE INTO sessions (bundle_id, session_id, configuration, options)  values (?, ?, ?, (SELECT options FROM sessions WHERE bundle_id = ? AND session_id = ?))"
- "REPLACE INTO sessions (bundle_id, session_id, options, configuration) \tvalues (?, ?, ?, (SELECT configuration FROM sessions WHERE bundle_id = ? AND session_id = ?))"
- "setWorkState"
```
