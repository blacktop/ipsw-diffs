## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-259.2.0.2.0
-  __TEXT.__text: 0xb1d2c
-  __TEXT.__objc_methlist: 0x6a64
-  __TEXT.__const: 0x4598
-  __TEXT.__gcc_except_tab: 0x16e8
-  __TEXT.__cstring: 0xa007
-  __TEXT.__oslogstring: 0x5792
+259.5.0.0.0
+  __TEXT.__text: 0xb2c74
+  __TEXT.__objc_methlist: 0x6b3c
+  __TEXT.__const: 0x45a8
+  __TEXT.__gcc_except_tab: 0x1740
+  __TEXT.__cstring: 0xa067
+  __TEXT.__oslogstring: 0x5912
   __TEXT.__dlopen_cstrs: 0x3d8
   __TEXT.__swift5_typeref: 0x1025
   __TEXT.__constg_swiftt: 0x199c

   __TEXT.__swift5_capture: 0x230
   __TEXT.__swift5_mpenum: 0x100
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__unwind_info: 0x4170
-  __TEXT.__eh_frame: 0x2fc0
+  __TEXT.__unwind_info: 0x41c0
+  __TEXT.__eh_frame: 0x2ff8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1cd0
-  __DATA_CONST.__objc_classlist: 0x540
+  __DATA_CONST.__const: 0x1d20
+  __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33e0
+  __DATA_CONST.__objc_selrefs: 0x3468
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x380
+  __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__objc_arraydata: 0x168
-  __DATA_CONST.__got: 0x710
+  __DATA_CONST.__got: 0x718
   __AUTH_CONST.__const: 0x43b8
   __AUTH_CONST.__cfstring: 0x60c0
-  __AUTH_CONST.__objc_const: 0x13120
+  __AUTH_CONST.__objc_const: 0x132a0
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xd90
-  __AUTH.__objc_data: 0x398
+  __AUTH_CONST.__auth_got: 0xdd0
+  __AUTH.__objc_data: 0x3e8
   __AUTH.__data: 0x268
-  __DATA.__objc_ivar: 0x6e0
+  __DATA.__objc_ivar: 0x6f4
   __DATA.__data: 0x1b50
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x2910

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4919
-  Symbols:   5302
-  CStrings:  1402
+  Functions: 4939
+  Symbols:   5345
+  CStrings:  1408
 
Symbols:
+ -[CCSetChangeTokenState .cxx_destruct]
+ -[CCSetChangeTokenState failedResolutionCount]
+ -[CCSetChangeTokenState filterStatus]
+ -[CCSetChangeTokenState init]
+ -[CCSetChangeTokenState setFailedResolutionCount:]
+ -[CCSetChangeTokenState setFilterStatus:]
+ -[CCSetChangeTokenState setIdentifierAllowList]
+ -[CCSetChangeTokenState setSetIdentifierAllowList:]
+ -[CCSetChangeTokenState setUnfilteredSince:]
+ -[CCSetChangeTokenState unfilteredSince]
+ -[CCSetChangeXPCNotifier _failResolutionForToken:]
+ -[CCSetChangeXPCNotifier _fireEvent:token:]
+ -[CCSetChangeXPCNotifier _fireEvent:withReplyToToken:handler:]
+ -[CCSetChangeXPCNotifier _notifyAndResolveFilterForToken:set:event:]
+ -[CCSetChangeXPCNotifier _notifyChangeToSet:event:token:]
+ -[CCSetChangeXPCNotifier _now]
+ -[CCSetChangeXPCNotifier _processForReply:]
+ -[CCSetChangeXPCNotifier _readableSetIdentifiersForReply:token:set:]
+ -[CCSetChangeXPCNotifier _resolveFilterForToken:readableSetIdentifiers:]
+ _OBJC_CLASS_$_CCSetChangeTokenState
+ _OBJC_IVAR_$_CCSetChangeTokenState._failedResolutionCount
+ _OBJC_IVAR_$_CCSetChangeTokenState._filterStatus
+ _OBJC_IVAR_$_CCSetChangeTokenState._setIdentifierAllowList
+ _OBJC_IVAR_$_CCSetChangeTokenState._unfilteredSince
+ _OBJC_IVAR_$_CCSetChangeXPCNotifier._resolutionQueue
+ _OBJC_METACLASS_$_CCSetChangeTokenState
+ __OBJC_$_INSTANCE_METHODS_CCSetChangeTokenState
+ __OBJC_$_INSTANCE_VARIABLES_CCSetChangeTokenState
+ __OBJC_$_PROP_LIST_CCSetChangeTokenState
+ __OBJC_CLASS_RO_$_CCSetChangeTokenState
+ __OBJC_METACLASS_RO_$_CCSetChangeTokenState
+ ___44-[CCSetChangeXPCNotifier notifyChangeToSet:]_block_invoke_2
+ ___68-[CCSetChangeXPCNotifier _notifyAndResolveFilterForToken:set:event:]_block_invoke
+ ___68-[CCSetChangeXPCNotifier _notifyAndResolveFilterForToken:set:event:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48w_e33_v16?0"NSObject<OS_xpc_object>"8lw48l8s32l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56r64r72r80r_e48_v32?0"NSNumber"8"CCSetChangeTokenState"16^B24ls32l8s40l8s48l8r56l8r64l8r72l8r80l8
+ __xpc_type_dictionary
+ _clock_gettime_nsec_np
+ _dispatch_assert_queue_not$V2
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_expects_reply
+ _xpc_dictionary_get_audit_token
+ _xpc_dictionary_send_reply
+ _xpc_event_publisher_fire_with_reply
+ _xpc_get_type
- -[CCSetChangeXPCListener initWithIdentifier:batchHandlerBlock:queue:]
- -[CCSetChangeXPCListener initWithIdentifier:handlerBlock:queue:]
CStrings:
+ "%@ (%lu listeners): set change notifications for set %@ sent to %d unknown, %d pending, %d unfiltered, %d filtered."
+ "%@ could not identify listener with token: %@ (%@)"
+ "%@ could not identify listener with token: %@ after %lu attempts, it will get every set change for %llu seconds"
+ "%@ firing xpc_event to %@ returned %d with error %s for set: %@"
+ "%@ xpc_event_publisher_fire_with_reply returned NULL or non-dictionary from token %@ for set: %@: %{public}@"
+ "%@: listener %@ replied with set list: %@"
+ "com.apple.cascade.setChange.xpc.notifier.resolution"
+ "v32@?0@\"NSNumber\"8@\"CCSetChangeTokenState\"16^B24"
- "%@ firing xpc_event for set: %@ to %lu listener(s)"
- "%@ firing xpc_event returned %d with error %s for set: %@"
```
