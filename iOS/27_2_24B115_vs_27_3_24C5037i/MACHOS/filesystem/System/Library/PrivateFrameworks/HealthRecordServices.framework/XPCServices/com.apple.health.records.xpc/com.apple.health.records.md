## com.apple.health.records

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.xpc/com.apple.health.records`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x2ae8
+7027.2.13.0.0
+  __TEXT.__text: 0x2dac
   __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x480
-  __TEXT.__objc_methlist: 0x41c
+  __TEXT.__objc_stubs: 0x4a0
+  __TEXT.__objc_methlist: 0x42c
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__cstring: 0x10c
-  __TEXT.__oslogstring: 0x80a
+  __TEXT.__oslogstring: 0x8f2
   __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0xbdf
-  __TEXT.__objc_methtype: 0x7d9
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_methname: 0xc37
+  __TEXT.__objc_methtype: 0x843
+  __TEXT.__unwind_info: 0x170
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x60
-  __DATA.__objc_const: 0x498
-  __DATA.__objc_selrefs: 0x2c0
+  __DATA_CONST.__got: 0x68
+  __DATA.__objc_const: 0x4a0
+  __DATA.__objc_selrefs: 0x2d0
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices
+  - /System/Library/PrivateFrameworks/HealthRecordsAssembler.framework/HealthRecordsAssembler
   - /System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 71
-  Symbols:   62
-  CStrings:  189
+  Functions: 74
+  Symbols:   63
+  CStrings:  195
 
Symbols:
+ _OBJC_CLASS_$_HDMedicalHistoryFHIRSynthesizer
CStrings:
+ "%{public}@: Synthesize MedicalHistory FHIR with Request Finished Successfully"
+ "%{public}@: Synthesize MedicalHistory FHIR with Request Starting"
+ "%{public}@: remote_synthesizeMedicalHistoryFHIRWithRequest failed with error: %{public}@"
+ "remote_synthesizeMedicalHistoryFHIRWithRequest:completion:"
+ "synthesizeWithRequest:error:"
+ "v32@0:8@\"HKMedicalHistoryFHIRSynthesisRequest\"16@?<v@?@\"HKMedicalHistoryFHIRSynthesisResult\"@\"NSError\">24"
```
