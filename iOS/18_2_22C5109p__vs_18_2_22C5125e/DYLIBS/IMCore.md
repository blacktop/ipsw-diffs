## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1402.300.129.2.15
-  __TEXT.__text: 0x1bf100
+1402.300.158.2.2
+  __TEXT.__text: 0x1bff14
   __TEXT.__auth_stubs: 0x2710
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_methlist: 0x13378
+  __TEXT.__objc_methlist: 0x133d8
   __TEXT.__const: 0x16b0
-  __TEXT.__gcc_except_tab: 0x1602c
-  __TEXT.__cstring: 0x10697
-  __TEXT.__oslogstring: 0x1e219
+  __TEXT.__gcc_except_tab: 0x160e0
+  __TEXT.__cstring: 0x10627
+  __TEXT.__oslogstring: 0x1e319
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__constg_swiftt: 0x550

   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x6c
   __TEXT.__swift5_capture: 0x4ac
-  __TEXT.__unwind_info: 0x7dd0
+  __TEXT.__unwind_info: 0x7d48
   __TEXT.__eh_frame: 0x8c8
-  __TEXT.__objc_classname: 0x251f
-  __TEXT.__objc_methname: 0x3cdad
-  __TEXT.__objc_methtype: 0x6495
-  __TEXT.__objc_stubs: 0x24720
-  __DATA_CONST.__got: 0x1ed8
-  __DATA_CONST.__const: 0x5098
+  __TEXT.__objc_classname: 0x2520
+  __TEXT.__objc_methname: 0x3ced7
+  __TEXT.__objc_methtype: 0x64d5
+  __TEXT.__objc_stubs: 0x247e0
+  __DATA_CONST.__got: 0x1ef8
+  __DATA_CONST.__const: 0x50c8
   __DATA_CONST.__objc_classlist: 0x728
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x428
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc8c0
+  __DATA_CONST.__objc_selrefs: 0xc8f0
   __DATA_CONST.__objc_protorefs: 0x198
   __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x13a8
   __AUTH_CONST.__auth_ptr: 0x318
   __AUTH_CONST.__const: 0x41e8
-  __AUTH_CONST.__cfstring: 0xbd00
-  __AUTH_CONST.__objc_const: 0x210c0
+  __AUTH_CONST.__cfstring: 0xbc80
+  __AUTH_CONST.__objc_const: 0x21130
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x2940
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x112c
-  __DATA.__data: 0x2920
-  __DATA.__bss: 0x2d58
+  __DATA.__objc_ivar: 0x1134
+  __DATA.__data: 0x2900
+  __DATA.__bss: 0x2d68
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x2348
-  __DATA_DIRTY.__data: 0x3c8
+  __DATA_DIRTY.__data: 0x3b8
   __DATA_DIRTY.__bss: 0x3d8
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8889
-  Symbols:   2348
-  CStrings:  14348
+  Functions: 8899
+  Symbols:   2353
+  CStrings:  14359
 
Symbols:
+ _IMRecoverableMetadataKeyEarliestDeleteDateInterval
+ _IMRecoverableMetadataKeyLatestDeleteDateInterval
+ _IMRecoverableMetadataKeyRecoverableCount
+ _IMRecoverableMetadataKeyUnreadRecoverableCount
+ __swift_FORCE_LOAD_$_swiftAppleArchive
CStrings:
+ "\x16\x14"
+ "B44@0:8@16@24@32C40"
+ "IMFaceTimeUtilities: Skipping setting callerID since FT account doesn't contain senderAddress: %!@(MISSING), aliases: %!@(MISSING)"
+ "Merging %!@(MISSING) items of %!@(MISSING) items"
+ "Status observer %!p(MISSING) being dealloced without having been invalidated, this is likely a bug"
+ "Status observer %!p(MISSING) for handle %!@(MISSING) is being deallocated"
+ "Status observer %!p(MISSING) for handle %!@(MISSING) is being invalidated"
+ "TB,N,V_sentViaRemoteIntent"
+ "TQ,N,V_flags"
+ "Updating chat %!@(MISSING) empty display name to %!@(MISSING)"
+ "_completedMovingChatsToRecentlyDeleted:deletionDate:"
+ "_completedRecoveringChatsFromRecentlyDeleted:"
+ "_mergeItems:"
+ "_sentViaRemoteIntent"
+ "_shouldAppendServiceForChat:item:previousItem:chatStyle:"
+ "hasCommSafetySensitiveMessageFromSomeoneElse"
+ "movedMessagesToRecentlyDeletedForChatsWithGUIDs:queryID:deletionDate:"
+ "recoveredMessagesWithChatGUIDs:queryID:"
+ "sendSignal:toChannel:withNullableUniqueStringID:withPayload:"
+ "sentViaRemoteIntent"
+ "setSentViaRemoteIntent:"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@\"NSDate\"32"
- "\x1a"
- "Observer being dealloced without having been invalidated, this is likely a bug"
- "Status observer for handle %!@(MISSING) is being deallocated"
- "_shouldAppendServiceForItem:previousItem:chatStyle:"
- "earliestDeleteDateInterval"
- "latestDeleteDateInterval"
- "movedMessagesToRecentlyDeletedForChatsWithGUIDs:queryID:"
- "recoveredMessagesWithQueryID:"
- "sendSignal:toChannel:withUniqueStringID:withPayload:"

```
