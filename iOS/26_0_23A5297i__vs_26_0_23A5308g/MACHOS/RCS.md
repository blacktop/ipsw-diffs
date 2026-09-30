## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/RCS`

```diff

-1445.100.6.2.4
-  __TEXT.__text: 0xd6480
-  __TEXT.__auth_stubs: 0x1b10
+1447.100.7.2.3
+  __TEXT.__text: 0xdfaa0
+  __TEXT.__auth_stubs: 0x1bd0
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__objc_methlist: 0x854
-  __TEXT.__const: 0x4ec8
+  __TEXT.__objc_methlist: 0x85c
+  __TEXT.__const: 0x5078
   __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x4990
+  __TEXT.__objc_methname: 0x4ac1
   __TEXT.__objc_methtype: 0xe70
-  __TEXT.__cstring: 0x3125
-  __TEXT.__constg_swiftt: 0x1d64
-  __TEXT.__swift5_typeref: 0x1d41
+  __TEXT.__cstring: 0x31e5
+  __TEXT.__constg_swiftt: 0x1dc4
+  __TEXT.__swift5_typeref: 0x1dd1
   __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_reflstr: 0x117c
-  __TEXT.__swift5_assocty: 0x2c0
-  __TEXT.__oslogstring: 0x56d9
-  __TEXT.__swift5_fieldmd: 0x15dc
-  __TEXT.__swift5_proto: 0x2e4
-  __TEXT.__swift5_types: 0x1a0
-  __TEXT.__swift_as_entry: 0x22c
-  __TEXT.__swift_as_ret: 0x284
-  __TEXT.__swift5_capture: 0x8fc
+  __TEXT.__swift5_reflstr: 0x11cc
+  __TEXT.__swift5_assocty: 0x2d8
+  __TEXT.__oslogstring: 0x5a79
+  __TEXT.__swift5_fieldmd: 0x1640
+  __TEXT.__swift5_proto: 0x2f8
+  __TEXT.__swift5_types: 0x1a4
+  __TEXT.__swift_as_entry: 0x248
+  __TEXT.__swift_as_ret: 0x2a8
+  __TEXT.__swift5_capture: 0x93c
   __TEXT.__swift5_mpenum: 0xbc
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__unwind_info: 0x3098
-  __TEXT.__eh_frame: 0x81d0
-  __DATA_CONST.__auth_got: 0xd90
-  __DATA_CONST.__got: 0x7a8
-  __DATA_CONST.__auth_ptr: 0x540
-  __DATA_CONST.__const: 0x4f00
+  __TEXT.__unwind_info: 0x3310
+  __TEXT.__eh_frame: 0x8c40
+  __DATA_CONST.__auth_got: 0xdf0
+  __DATA_CONST.__got: 0x7f0
+  __DATA_CONST.__auth_ptr: 0x5a8
+  __DATA_CONST.__const: 0x5058
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1e78
-  __DATA.__objc_selrefs: 0x14f8
+  __DATA.__objc_const: 0x1eb8
+  __DATA.__objc_selrefs: 0x1558
   __DATA.__objc_data: 0x3e8
-  __DATA.__data: 0x32b8
-  __DATA.__bss: 0x4880
-  __DATA.__common: 0x98
+  __DATA.__data: 0x3400
+  __DATA.__bss: 0x4b00
+  __DATA.__common: 0xb8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 113653B9-EC84-3FC5-9BA2-1D557EE88ABB
-  Functions: 3161
-  Symbols:   400
-  CStrings:  1449
+  UUID: B0E4BCD5-7D5A-340A-B0FA-5FDA7C18CD17
+  Functions: 3271
+  Symbols:   405
+  CStrings:  1487
 
Symbols:
+ _NSDefaultRunLoopMode
+ _OBJC_CLASS_$_IMDSpamFilteringDebugUIService
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSTimer
+ _objc_release_x10
- _IMPersonStatusChangeID
CStrings:
+ "?"
+ "@\"CTXPCServiceSubscriptionContext\""
+ "@\"IMDChat\""
+ "@\"IMDTelephonyServiceSession\""
+ "@\"IMMessageItem\""
+ "@\"RCSServiceSession\""
+ "Adding message %s to retry set with interval %ld"
+ "Attempting send for %s"
+ "B"
+ "Building timer with interval %ld"
+ "C"
+ "Error while sending message %s, %@"
+ "Failed to retry send with error %@, skipping %s) until next retry interval in %fs\")"
+ "Failed to send with error %u for rcsMessage %s"
+ "Finished considering retry for message %s"
+ "Message %s is no longer eligible for retries as of %s. Removing from retry set..."
+ "Messages to retry on next interval in %fs: %@"
+ "RCS6"
+ "Removing sent messages from retry set: %s"
+ "Retries not enabled for context %@, not retrying message %s).\nEnsure resiliency mode is enabled for this context from Telephony."
+ "Retry timer fired; retry set count: %ld"
+ "Skipping retry attempt for %s as we're still waiting for results from previous retry"
+ "Stopping all retries..."
+ "Successfully resent message %s"
+ "Successfully sent rcsMessage %s"
+ "addObject:"
+ "addTimer:forMode:"
+ "containsObject:"
+ "currentRunLoop"
+ "dictionaryForHandlesToGUIDsFromHandleInfo:"
+ "fireTimerWithTimer:"
+ "invalidate"
+ "minusSet:"
+ "presentDebugUI"
+ "recordFilteringMetricsForMessageItem:filteredToChat:filterExtensionMetadata:"
+ "retryIntervalTimer"
+ "retryItems"
+ "timeInterval"
+ "timerWithTimeInterval:target:selector:userInfo:repeats:"
+ "v48@?0q8q16@\"NSString\"24@\"NSDictionary\"32@\"NSDictionary\"40"
- "Error while sending %@"
- "v40@?0q8q16@\"NSString\"24@\"NSDictionary\"32"

```
