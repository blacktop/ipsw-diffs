## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1626.300.42.0.0
-  __TEXT.__text: 0x1b3e00
-  __TEXT.__objc_methlist: 0x1bd60
-  __TEXT.__cstring: 0x14b36
+1626.300.62.0.0
+  __TEXT.__text: 0x1b48b0
+  __TEXT.__objc_methlist: 0x1bda0
+  __TEXT.__cstring: 0x14b76
   __TEXT.__const: 0x4bcc
-  __TEXT.__oslogstring: 0x14df4
-  __TEXT.__gcc_except_tab: 0x18d4
+  __TEXT.__oslogstring: 0x14e44
+  __TEXT.__gcc_except_tab: 0x191c
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8a5
   __TEXT.__constg_swiftt: 0xebc

   __TEXT.__swift_as_cont: 0x1cc
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x9960
+  __TEXT.__unwind_info: 0x9980
   __TEXT.__eh_frame: 0x2f98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3a48
+  __DATA_CONST.__const: 0x3a70
   __DATA_CONST.__objc_classlist: 0x8c0
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba48
+  __DATA_CONST.__objc_selrefs: 0xba60
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0xaf8
   __DATA_CONST.__got: 0x10c8
-  __AUTH_CONST.__const: 0x4e90
-  __AUTH_CONST.__cfstring: 0x12be0
-  __AUTH_CONST.__objc_const: 0x2baa0
+  __AUTH_CONST.__const: 0x4eb0
+  __AUTH_CONST.__cfstring: 0x12c20
+  __AUTH_CONST.__objc_const: 0x2bb10
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__auth_got: 0x1698
   __AUTH.__objc_data: 0x2c60
   __AUTH.__data: 0xde0
-  __DATA.__objc_ivar: 0x1964
+  __DATA.__objc_ivar: 0x196c
   __DATA.__data: 0x3fc0
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x2da8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12136
-  Symbols:   16395
-  CStrings:  4737
+  Functions: 12144
+  Symbols:   16403
+  CStrings:  4742
 
Symbols:
+ -[TUContinuitySessionInfo initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:meContact:meHandle:isDedicatedSession:favorites:conversationLinks:recentCallsInfos:callBlockedStates:]
+ -[TUContinuitySessionInfo meContact]
+ -[TUContinuitySessionInfo meHandle]
+ -[TUConversationManager getLocalCallerIDWithCompletionHandler:]
+ -[TUConversationManagerXPCClient getLocalCallerIDWithCompletionHandler:]
+ GCC_except_table179
+ _OBJC_IVAR_$_TUContinuitySessionInfo._meContact
+ _OBJC_IVAR_$_TUContinuitySessionInfo._meHandle
+ _TUHandleIsNormalized
+ ___72-[TUConversationManagerXPCClient getLocalCallerIDWithCompletionHandler:]_block_invoke
+ ___TUUniqueContactIdentifiersByHandle_block_invoke
+ ___TUUniqueContactIdentifiersByHandle_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48r_e35_v32?0"NSString"8"NSString"16^B24ls32l8s40l8r48l8
+ _os_unfair_recursive_lock_lock
- -[TUContinuitySessionInfo initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:isDedicatedSession:favorites:conversationLinks:recentCallsInfos:callBlockedStates:]
- GCC_except_table151
- GCC_except_table177
- GCC_except_table88
- GCC_except_table90
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ " hasMeContact=%d"
+ " meHandle=%@"
+ "Asked for the local caller ID"
+ "Error in retrieving local caller ID: %@"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
```
