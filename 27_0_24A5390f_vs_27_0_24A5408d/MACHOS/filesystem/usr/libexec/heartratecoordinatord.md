## heartratecoordinatord

> `/usr/libexec/heartratecoordinatord`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-41.1.0.0.0
-  __TEXT.__text: 0x26e6c
+42.0.0.0.0
+  __TEXT.__text: 0x27c68
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x3fe0
+  __TEXT.__objc_stubs: 0x4180
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x19f4
+  __TEXT.__objc_methlist: 0x1abc
   __TEXT.__const: 0x375
-  __TEXT.__oslogstring: 0x3ae8
-  __TEXT.__cstring: 0x2191
-  __TEXT.__gcc_except_tab: 0x439c
-  __TEXT.__objc_methname: 0x5119
-  __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methtype: 0x1c3b
-  __TEXT.__unwind_info: 0x1238
+  __TEXT.__oslogstring: 0x3bab
+  __TEXT.__cstring: 0x22cd
+  __TEXT.__gcc_except_tab: 0x44d8
+  __TEXT.__objc_methname: 0x52de
+  __TEXT.__objc_classname: 0x3a8
+  __TEXT.__objc_methtype: 0x1c0f
+  __TEXT.__unwind_info: 0x12b8
   __DATA_CONST.__const: 0xce0
-  __DATA_CONST.__cfstring: 0x2020
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__cfstring: 0x21c0
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20

   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x238
-  __DATA.__objc_const: 0x2c18
-  __DATA.__objc_selrefs: 0x11f0
-  __DATA.__objc_ivar: 0x288
-  __DATA.__objc_data: 0x640
+  __DATA_CONST.__got: 0x240
+  __DATA.__objc_const: 0x2d50
+  __DATA.__objc_selrefs: 0x1258
+  __DATA.__objc_ivar: 0x298
+  __DATA.__objc_data: 0x690
   __DATA.__data: 0x600
   __DATA.__bss: 0xa8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 919
-  Symbols:   209
-  CStrings:  1600
+  Functions: 939
+  Symbols:   210
+  CStrings:  1632
 
Symbols:
+ _OBJC_CLASS_$_NSNull
CStrings:
+ "HRCRecentHighConfidenceStats"
+ "Source controller: platinum foreground HRNN active changed to %{BOOL}u"
+ "_deliverRecentHighConfidenceHeartRates"
+ "_foregroundHRNNActive"
+ "_foregroundHRNNActiveDidChange:"
+ "_handlePlatinumForegroundHRNNActiveChanged:"
+ "_notifiedForegroundHRNNActive"
+ "_notifyDelegateForegroundHRNNActiveIfChanged"
+ "_pendingRecentHighConfidenceHeartRatesRequest"
+ "_setForegroundHRNNActive:"
+ "clientDidServeRecentHighConfidenceHeartRatesWithSourceType:processName:"
+ "deferring recent high confidence HRs request for %{public}@ until foreground HRNN is active"
+ "foregroundHRNNActive"
+ "foregroundHRNNActive : %{BOOL}u"
+ "foregroundHRNNActiveDidChange:"
+ "isForegroundHRNNActive"
+ "isPublishableSample:"
+ "null"
+ "pct_context_background"
+ "pct_context_background_tachogram"
+ "pct_context_breathe"
+ "pct_context_ecg"
+ "pct_context_not_set"
+ "pct_context_oxygen_saturation"
+ "pct_context_sedentary"
+ "pct_context_sleep_mode_sedentary"
+ "pct_context_streaming_ppg"
+ "pct_context_walking"
+ "pct_context_wheelchair_motion"
+ "pct_context_workout"
+ "publishable_count"
+ "recordRecentHighConfidenceHeartRatesServed:sourceType:processName:windowStats:"
+ "setForegroundHRNNActive:"
+ "setForegroundHRNNActiveHandler:"
+ "statsForWindow:"
+ "total_count"
+ "v48@0:8d16q24@32@40"
+ "\xa1"
- "clientDidServeRecentHighConfidenceHeartRatesWithCount:sourceType:processName:"
- "hr_count"
- "recordRecentHighConfidenceHeartRatesServed:ageSeconds:sourceType:processName:"
- "v40@0:8q16q24@\"NSString\"32"
- "v40@0:8q16q24@32"
- "v48@0:8q16d24q32@40"
```
