## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon`

```diff

-995.1.0.0.0
-  __TEXT.__text: 0x71250
+999.4.0.0.0
+  __TEXT.__text: 0x724a8
   __TEXT.__auth_stubs: 0x1520
-  __TEXT.__objc_methlist: 0x3254
-  __TEXT.__const: 0x726
-  __TEXT.__oslogstring: 0x81df
-  __TEXT.__cstring: 0x3d93
-  __TEXT.__gcc_except_tab: 0x25e4
+  __TEXT.__objc_methlist: 0x3ae4
+  __TEXT.__const: 0x7d6
+  __TEXT.__oslogstring: 0x82ef
+  __TEXT.__cstring: 0x3ad3
+  __TEXT.__gcc_except_tab: 0x25c4
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__swift5_typeref: 0x2aa
   __TEXT.__swift5_capture: 0xa8

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x19d0
-  __TEXT.__eh_frame: 0x270
-  __TEXT.__objc_classname: 0x601
-  __TEXT.__objc_methname: 0xafbd
-  __TEXT.__objc_methtype: 0x2444
-  __TEXT.__objc_stubs: 0x8fc0
-  __DATA_CONST.__got: 0xce8
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__unwind_info: 0x1ab0
+  __TEXT.__eh_frame: 0x2c8
+  __TEXT.__objc_classname: 0x600
+  __TEXT.__objc_methname: 0xb0ce
+  __TEXT.__objc_methtype: 0x2464
+  __TEXT.__objc_stubs: 0x90a0
+  __DATA_CONST.__got: 0xcf8
   __DATA_CONST.__const: 0x16a8
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2778
+  __DATA_CONST.__objc_selrefs: 0x2910
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0xaa0
   __AUTH_CONST.__auth_ptr: 0x208
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x3240
-  __AUTH_CONST.__objc_const: 0x5618
+  __AUTH_CONST.__cfstring: 0x3260
+  __AUTH_CONST.__objc_const: 0x4690
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x3b8
-  __DATA.__objc_ivar: 0x29c
+  __AUTH.__objc_data: 0x368
+  __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x710
-  __DATA.__bss: 0x780
-  __DATA_DIRTY.__objc_data: 0xd38
+  __DATA.__bss: 0x700
+  __DATA_DIRTY.__objc_data: 0xd88
   __DATA_DIRTY.__data: 0x278
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0x358
+  __DATA_DIRTY.__bss: 0x3e0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2042
-  Symbols:   2714
-  CStrings:  3048
+  Functions: 2114
+  Symbols:   2810
+  CStrings:  3045
 
Symbols:
+ _ACAccountTypeIdentifierDCA
+ __dispatch_source_type_memorypressure
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_workloop_create
+ _kACDDetachedCAFullAccessEntitlement
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_arrayDestroy
CStrings:
+ "\x11\x15"
+ "\"%{public}s error, account %{private}@ lacks an account type identifier\""
+ "\"ACDAccountCache: Memory pressure notification received, flushing cache\""
+ "\"ACDDatabaseConnection: Memory pressure notification received, flushing cache\""
+ "\"The plugin %@ for accountType %@ is being overwritten with plugin %@\""
+ "\"Using fallback Game Center ACD plugin.\""
+ "\"Using modern Game Center ACD plugin.\""
+ "+[ACDKeychainManager _saveCredential:forAccount:clientID:error:]"
+ "@\"NSObject<OS_dispatch_source>\""
+ "Detached Child Account"
+ "Q"
+ "_addDCAAccountType"
+ "_clearCacheIncludingRemote:"
+ "_handoffCurrentReplyToQueue:block:"
+ "_memoryNotificationSource"
+ "_setupMemoryNotifications"
+ "_teardownMemoryNotifications"
+ "gameCenterPluginNameFromPlugins:modernPluginEnabled:fallbackPluginID:modernPluginID:"
+ "setupMemoryNotifications"
- "\x04"
- "\"Filtering out AAGKAuthenticationPlugin.\""
- "\"Filtering out GameCenterAccountAuthenticationPlugin.\""
- "%"
- "A"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
