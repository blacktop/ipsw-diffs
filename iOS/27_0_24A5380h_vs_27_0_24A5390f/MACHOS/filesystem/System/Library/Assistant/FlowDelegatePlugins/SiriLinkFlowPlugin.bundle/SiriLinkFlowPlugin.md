## SiriLinkFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-3600.8.4.0.0
-  __TEXT.__text: 0x217264
+3600.8.7.0.0
+  __TEXT.__text: 0x217228
   __TEXT.__auth_stubs: 0x5540
-  __TEXT.__objc_stubs: 0x5320
-  __TEXT.__objc_methlist: 0xed4
+  __TEXT.__objc_stubs: 0x5340
+  __TEXT.__objc_methlist: 0xedc
   __TEXT.__const: 0x1796c
   __TEXT.__cstring: 0x5dfa
-  __TEXT.__objc_methname: 0x5295
+  __TEXT.__objc_methname: 0x52d5
   __TEXT.__objc_classname: 0x21c9
-  __TEXT.__objc_methtype: 0xcce
+  __TEXT.__objc_methtype: 0xd0e
   __TEXT.__swift5_typeref: 0x5b6a
   __TEXT.__oslogstring: 0xd85a
   __TEXT.__swift5_capture: 0x1058

   __DATA_CONST.__auth_got: 0x2aa8
   __DATA_CONST.__got: 0x1888
   __DATA_CONST.__auth_ptr: 0x1728
-  __DATA.__objc_const: 0xe6a0
-  __DATA.__objc_selrefs: 0x18f8
+  __DATA.__objc_const: 0xe6a8
+  __DATA.__objc_selrefs: 0x1908
   __DATA.__objc_ivar: 0x9c
   __DATA.__objc_data: 0xff0
   __DATA.__data: 0xbd30

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 13538
-  Symbols:   29845
-  CStrings:  2862
+  Symbols:   29846
+  CStrings:  2865
 
Symbols:
+ _objc_msgSend$setConfirmationCondition:
Functions:
~ _$s18SiriLinkFlowPlugin09ShortcutsB15RCHFlowStrategyC16makeCustomOutput11appBundleId07successJ0014startedSessionM018isAudioStartAction11deviceState04linkT14DialogTemplate15responseFactory14serviceInvoker0a3KitC00J0_pSS_So08LNActionJ0CSSSgSbAM06DeviceV0_pAA0btX10TemplatingCAM18ResponseGenerating_pAM22AceServiceInvokerAsync_ptYaKFZTY6_ : 188 -> 184
~ _$s18SiriLinkFlowPlugin09ShortcutsB15RCHFlowStrategyC7flowFor5error0a3KitC003AnyC0Cs5Error_p_tFAF6Output_pyYaYbKcfU_TY4_ : 308 -> 304
~ _$s18SiriLinkFlowPlugin09ShortcutsB15RCHFlowStrategyC40makeOutputForFailureHandlingIntentDialog5error0a3KitC00I0_ps5Error_p_tYaKFTY2_ : 420 -> 416
~ _$s18SiriLinkFlowPlugin09ShortcutsB15RCHFlowStrategyC16makeCustomOutput11deviceState18isAudioStartAction15responseFactory12dialogResult8manifest8viewData11appBundleId07snippetP011environment0a3KitC00J0_pAN06DeviceL0_p_SbAN18ResponseGenerating_pSo015DialogExecutionT0CAN0J18GenerationManifestV10Foundation0W0VSgSSSo8LNActionCSgSo20LNSnippetEnvironmentCSgtYaFZTY0_ : 740 -> 680
~ _$s18SiriLinkFlowPlugin0B7RCHFlowC010initializeB10Connection33_A83A936DCCD3C7AD4B517ED3FBC5A826LL10connection15interactionModeyAA0bG0_p_So013LNInteractionS0VtYaFTY0_ : 1188 -> 1200
CStrings:
+ "executor:updateOpensIntentRequest:"
+ "setConfirmationCondition:"
+ "v32@0:8@\"LNActionExecutor\"16@\"LNUpdateOpensIntentRequest\"24"
```
