## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation`

```diff

-3610.10.1.0.0
-  __TEXT.__text: 0x8db24
-  __TEXT.__objc_methlist: 0x4788
-  __TEXT.__const: 0x38dc
-  __TEXT.__cstring: 0x6736
-  __TEXT.__oslogstring: 0x701b
+3610.17.2.0.0
+  __TEXT.__text: 0x8e6a8
+  __TEXT.__objc_methlist: 0x4878
+  __TEXT.__const: 0x38fc
+  __TEXT.__cstring: 0x6836
+  __TEXT.__oslogstring: 0x70bb
   __TEXT.__gcc_except_tab: 0xa28
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x15ba
   __TEXT.__swift5_capture: 0x78c
   __TEXT.__constg_swiftt: 0x14d4
-  __TEXT.__swift5_reflstr: 0x114a
-  __TEXT.__swift5_fieldmd: 0xfac
+  __TEXT.__swift5_reflstr: 0x116a
+  __TEXT.__swift5_fieldmd: 0xfb8
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_proto: 0x254
   __TEXT.__swift5_types: 0x130

   __TEXT.__swift_as_ret: 0xfc
   __TEXT.__swift_as_cont: 0x194
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x2f78
+  __TEXT.__swift5_assocty: 0x228
+  __TEXT.__unwind_info: 0x2fb0
   __TEXT.__eh_frame: 0x24a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x19d8
-  __DATA_CONST.__objc_classlist: 0x330
+  __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ff0
+  __DATA_CONST.__objc_selrefs: 0x30a8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0xaa0
+  __DATA_CONST.__got: 0xab0
   __AUTH_CONST.__const: 0x3b41
-  __AUTH_CONST.__cfstring: 0x23c0
-  __AUTH_CONST.__objc_const: 0x90a0
+  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__objc_const: 0x92e0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0xf28
-  __AUTH.__objc_data: 0x1170
+  __AUTH.__objc_data: 0x1210
   __AUTH.__data: 0xc28
-  __DATA.__objc_ivar: 0x43c
-  __DATA.__data: 0x1740
+  __DATA.__objc_ivar: 0x454
+  __DATA.__data: 0x1738
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xf48
   __DATA_DIRTY.__data: 0x9d0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3402
-  Symbols:   3764
-  CStrings:  1136
+  Functions: 3422
+  Symbols:   3804
+  CStrings:  1149
 
Symbols:
+ +[SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags) isIntercomPlannerToolsEnabled]
+ -[SRUIFInstrumentationManager _isLoggableLinkTappedURL:]
+ -[SRUIFInstrumentationManager _weblinkMetadataForDetails:]
+ -[SRUIFInstrumentationManager emitLinkTappedWithType:isPersonalEntity:opensExternally:URL:]
+ -[SRUIFInstrumentationManager emitLinkTappedWithType:isPersonalEntity:opensExternally:details:]
+ -[SRUIFLinkTapDetails .cxx_destruct]
+ -[SRUIFLinkTapDetails URL]
+ -[SRUIFLinkTapDetails initWithURL:weblink:]
+ -[SRUIFLinkTapDetails weblink]
+ -[SRUIFUIBridgeClient _considerTTSPrewarmForProgressUpdate:]
+ -[SRUIFUIBridgeClient _discardPendingTTSPrewarmWithReason:]
+ -[SRUIFUIBridgeClient _firePendingTTSPrewarmIfThinking:]
+ -[SRUIFUIBridgeClient discardPendingTTSPrewarm]
+ -[SRUIFUIBridgeClient scheduleTTSPrewarm:]
+ -[SRUIFWeblinkTapDetails .cxx_destruct]
+ -[SRUIFWeblinkTapDetails initWithPosition:openSource:]
+ -[SRUIFWeblinkTapDetails openSource]
+ -[SRUIFWeblinkTapDetails position]
+ GCC_except_table108
+ GCC_except_table110
+ GCC_except_table117
+ _OBJC_CLASS_$_SISchemaUEIWeblinkMetadata
+ _OBJC_CLASS_$_SRUIFLinkTapDetails
+ _OBJC_CLASS_$_SRUIFWeblinkTapDetails
+ _OBJC_IVAR_$_SRUIFLinkTapDetails._URL
+ _OBJC_IVAR_$_SRUIFLinkTapDetails._weblink
+ _OBJC_IVAR_$_SRUIFUIBridgeClient._pendingTTSPrewarm
+ _OBJC_IVAR_$_SRUIFUIBridgeClient._ttsPrewarmLock
+ _OBJC_IVAR_$_SRUIFWeblinkTapDetails._openSource
+ _OBJC_IVAR_$_SRUIFWeblinkTapDetails._position
+ _OBJC_METACLASS_$_SRUIFLinkTapDetails
+ _OBJC_METACLASS_$_SRUIFWeblinkTapDetails
+ __OBJC_$_INSTANCE_METHODS_SRUIFLinkTapDetails
+ __OBJC_$_INSTANCE_METHODS_SRUIFWeblinkTapDetails
+ __OBJC_$_INSTANCE_VARIABLES_SRUIFLinkTapDetails
+ __OBJC_$_INSTANCE_VARIABLES_SRUIFWeblinkTapDetails
+ __OBJC_$_PROP_LIST_SRUIFLinkTapDetails
+ __OBJC_$_PROP_LIST_SRUIFWeblinkTapDetails
+ __OBJC_CLASS_RO_$_SRUIFLinkTapDetails
+ __OBJC_CLASS_RO_$_SRUIFWeblinkTapDetails
+ __OBJC_METACLASS_RO_$_SRUIFLinkTapDetails
+ __OBJC_METACLASS_RO_$_SRUIFWeblinkTapDetails
+ ___95-[SRUIFInstrumentationManager emitLinkTappedWithType:isPersonalEntity:opensExternally:details:]_block_invoke
+ ___block_descriptor_70_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- GCC_except_table102
- GCC_except_table104
- ___87-[SRUIFInstrumentationManager emitLinkTappedWithType:isPersonalEntity:opensExternally:]_block_invoke
- ___block_descriptor_61_e8_32s40w_e5_v8?0lw40l8s32l8
CStrings:
+ "%s #ttsprewarm deferral disabled, prewarming now"
+ "%s #ttsprewarm dropped: %s"
+ "%s #ttsprewarm fired at thinking"
+ "%s #ttsprewarm scheduled (replaced pending: %d)"
+ "-[SRUIFUIBridgeClient _discardPendingTTSPrewarmWithReason:]"
+ "-[SRUIFUIBridgeClient _firePendingTTSPrewarmIfThinking:]"
+ "-[SRUIFUIBridgeClient scheduleTTSPrewarm:]"
+ "IntercomPlannerTools"
+ "Siri ended"
+ "SiriTTSPrewarmDeferralDisabled"
+ "http"
+ "https"
+ "request ended"
```
