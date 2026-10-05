## Siri

> `/Applications/Siri.app/Siri`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_stublist`

```diff

-3605.24.1.0.0
-  __TEXT.__text: 0xec084
-  __TEXT.__auth_stubs: 0x3060
-  __TEXT.__objc_stubs: 0x1b860
-  __TEXT.__objc_methlist: 0xe480
+3605.30.1.0.0
+  __TEXT.__text: 0xecab4
+  __TEXT.__auth_stubs: 0x3080
+  __TEXT.__objc_stubs: 0x1b880
+  __TEXT.__objc_methlist: 0xe4b0
   __TEXT.__const: 0x3134
-  __TEXT.__cstring: 0x2481d
-  __TEXT.__oslogstring: 0xdc34
-  __TEXT.__objc_classname: 0x1fa3
-  __TEXT.__objc_methtype: 0xafb1
+  __TEXT.__cstring: 0x2492d
+  __TEXT.__oslogstring: 0xdca4
+  __TEXT.__objc_classname: 0x1fb3
+  __TEXT.__objc_methtype: 0xb101
   __TEXT.__gcc_except_tab: 0x13bc
-  __TEXT.__objc_methname: 0x2bb7f
+  __TEXT.__objc_methname: 0x2ba7f
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x265c
-  __TEXT.__constg_swiftt: 0x2578
-  __TEXT.__swift5_reflstr: 0x1a61
-  __TEXT.__swift5_fieldmd: 0x1348
+  __TEXT.__swift5_typeref: 0x2700
+  __TEXT.__constg_swiftt: 0x25c8
+  __TEXT.__swift5_reflstr: 0x1b11
+  __TEXT.__swift5_fieldmd: 0x1378
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x1e8
   __TEXT.__swift5_protos: 0x40

   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift_as_cont: 0x38
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x47a0
+  __TEXT.__unwind_info: 0x47a8
   __TEXT.__eh_frame: 0xcc0
   __DATA_CONST.__const: 0x4e30
   __DATA_CONST.__cfstring: 0x3380

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x150
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1840
+  __DATA_CONST.__auth_got: 0x1850
   __DATA_CONST.__got: 0x1858
   __DATA_CONST.__auth_ptr: 0x8f8
-  __DATA.__objc_const: 0x10eb8
-  __DATA.__objc_selrefs: 0x90b8
+  __DATA.__objc_const: 0x10f38
+  __DATA.__objc_selrefs: 0x90c8
   __DATA.__objc_ivar: 0x8dc
-  __DATA.__objc_data: 0x4bd8
-  __DATA.__data: 0x47f0
+  __DATA.__objc_data: 0x4c48
+  __DATA.__data: 0x4810
   __DATA.__objc_stublist: 0x10
   __DATA.__common: 0x370
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5209
-  Symbols:   1865
-  CStrings:  9087
+  Functions: 5216
+  Symbols:   1867
+  CStrings:  9100
 
Symbols:
+ _$s10Foundation4UUIDV2eeoiySbAC_ACtFZ
+ _swift_setAtReferenceWritableKeyPath
CStrings:
+ "#PreprocessNotification We have a preprocessed response. Presenting the response and immediately marking the response as rendered."
+ "%s #aceCommandRecord recording action completed at the presentation's request for aceCommand=%@ success=%i"
+ "-[SRSiriViewController siriPresentation:recordActionCompletedForAceCommand:success:]"
+ "carPlayViewControllerRequestsPerformIFAction(_:action:turnIdentifier:)"
+ "dispatcher:didFailPerformingAppIntentWithError:"
+ "isAttendingCarProvider"
+ "maxHeightConstraint"
+ "minHeightConstraint"
+ "pendingInteractionTurn"
+ "performIFAction:turnIdentifier:"
+ "searchui_cardLoader"
+ "siriPresentation:performIFAction:turnIdentifier:completion:"
+ "siriPresentation:recordActionCompletedForAceCommand:success:"
+ "startNewInstrumentationTurn(from:)"
+ "v32@0:8@\"<AFIntelligenceFlowActionDescriptor>\"16@\"NSUUID\"24"
+ "v32@0:8@\"SRUIFAppIntentDispatcher\"16@\"NSError\"24"
+ "v36@0:8@\"<SiriUIPresentation>\"16@\"AceObject<SAAceCommand>\"24B32"
+ "v48@0:8@\"<SiriUIPresentation>\"16@\"<AFIntelligenceFlowActionDescriptor>\"24@\"NSUUID\"32@?<v@?B>40"
+ "waveFormIsVisible"
- "#instrumentation New Turn %@ "
- "_directionalAccessoryEdgeInsets"
- "_scrollViewAccessoryInsetsDidChange:"
- "carPlayViewControllerRequestsPerformIFAction(_:action:)"
- "cardLoader"
- "isAttendingCar"
```
