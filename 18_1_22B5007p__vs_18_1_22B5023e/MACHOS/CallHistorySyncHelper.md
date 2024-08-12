## CallHistorySyncHelper

> `/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper`

```diff

-1255.100.11.0.0
-  __TEXT.__text: 0x2bc4c
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x5760
-  __TEXT.__objc_methlist: 0x1a40
-  __TEXT.__const: 0x1c2
-  __TEXT.__gcc_except_tab: 0x44c
-  __TEXT.__cstring: 0x1a30
-  __TEXT.__objc_methname: 0x6ad1
-  __TEXT.__oslogstring: 0x48d2
+1355.200.1.0.0
+  __TEXT.__text: 0x2c620
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_stubs: 0x57c0
+  __TEXT.__objc_methlist: 0x1a48
+  __TEXT.__const: 0x1e2
+  __TEXT.__gcc_except_tab: 0x494
+  __TEXT.__cstring: 0x1ab0
+  __TEXT.__objc_methname: 0x6b54
+  __TEXT.__oslogstring: 0x49f2
   __TEXT.__objc_classname: 0x2d5
   __TEXT.__objc_methtype: 0x15e7
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__swift5_typeref: 0xd7
-  __TEXT.__swift5_capture: 0x50
+  __TEXT.__swift5_typeref: 0x115
+  __TEXT.__swift5_capture: 0x70
   __TEXT.__constg_swiftt: 0x54
-  __TEXT.__swift5_reflstr: 0x4d
-  __TEXT.__swift5_fieldmd: 0x4c
+  __TEXT.__swift5_reflstr: 0x96
+  __TEXT.__swift5_fieldmd: 0x64
   __TEXT.__swift5_types: 0x4
-  __TEXT.__info_plist: 0x51b
-  __TEXT.__unwind_info: 0x890
+  __TEXT.__info_plist: 0x51a
+  __TEXT.__unwind_info: 0x8c0
   __TEXT.__eh_frame: 0x168
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0xf40
+  __DATA_CONST.__auth_got: 0x6a0
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x10a0
   __DATA_CONST.__cfstring: 0x17a0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x5228
-  __DATA.__objc_selrefs: 0x1a68
+  __DATA.__objc_const: 0x5268
+  __DATA.__objc_selrefs: 0x1a98
   __DATA.__objc_ivar: 0x210
-  __DATA.__objc_data: 0x7c8
-  __DATA.__data: 0x528
+  __DATA.__objc_data: 0x7d8
+  __DATA.__data: 0x548
   __DATA.__bss: 0x70
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 824
-  Symbols:   383
-  CStrings:  2036
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 839
+  Symbols:   401
+  CStrings:  2053
 
Symbols:
+ _$sBi32_WV
+ _$sSSN
+ _$sSo17OS_dispatch_queueC8DispatchE4mainABvgZ
+ _$ss5Int32VMn
+ _CXCallDirectoryManagerIdentificationEntriesChangedNotification
+ _OBJC_CLASS_$_CXCallDirectoryExtensionManager
+ _OBJC_CLASS_$_OS_dispatch_queue
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _notify_register_dispatch
+ _swift_endAccess
CStrings:
+ "Fetching count for searchString: %!@(MISSING)"
+ "Fetching items for searchString: %!@(MISSING)"
+ "Handling CXCallDirectoryManagerIdentificationEntriesChangedNotification"
+ "Items to reindex for contact change: %!l(MISSING)u is greater than threshold, triggering a full reindex"
+ "Updating Index for phoneNumber: %!{(MISSING)private}lld"
+ "callDirectoryManager"
+ "callDirectoryNotificationToken"
+ "getLastUpdatedCallDirectoryInfoWithReply:"
+ "handleCallDirectoryIdentitiesChanged"
+ "lastFourDigitsFrom:"
+ "queryContext"
+ "querySpotlightCountWithSearchString:completion:"
+ "setCountChangedHandler:"
+ "setCounting:"
+ "v12@?0i8"
+ "v16@?0Q8"
+ "v16@?0q8"
+ "v24@?0q8@\"NSError\"16"
- "indexedItemsForCallsHavingHandles:orContactIdentifier:completion:"

```
