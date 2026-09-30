## IOKitten

> `/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`

```diff

-400.1.0.0.0
-  __TEXT.__text: 0x50ac
+400.3.0.0.0
+  __TEXT.__text: 0x5800
   __TEXT.__auth_stubs: 0x7e0
   __TEXT.__objc_methlist: 0x7e0
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2e5
-  __TEXT.__oslogstring: 0x54
-  __TEXT.__unwind_info: 0x230
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x86e
+  __TEXT.__oslogstring: 0x7e
+  __TEXT.__unwind_info: 0x248
   __TEXT.__objc_classname: 0x116
   __TEXT.__objc_methname: 0x10eb
   __TEXT.__objc_methtype: 0x4f0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB09CEFB-372C-363E-9CBE-D16D050E95AF
-  Functions: 178
-  Symbols:   778
-  CStrings:  299
+  UUID: 72423B25-B04E-3462-960D-420E4D380F37
+  Functions: 198
+  Symbols:   774
+  CStrings:  318
 
CStrings:
+ "-[IOKConnection callAsyncMethodWithSelector:wakePort:reference:referenceCount:scalarInputs:scalarInputCount:scalarOutputs:scalarOutputCount:error:]"
+ "-[IOKConnection callAsyncMethodWithSelector:wakePort:reference:referenceCount:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:structOutput:structOutputSize:error:]"
+ "-[IOKConnection callAsyncMethodWithSelector:wakePort:reference:referenceCount:structInput:structInputSize:structOutput:structOutputSize:error:]"
+ "-[IOKConnection callMethodWithSelector:scalarInputs:scalarInputCount:scalarOutputs:scalarOutputCount:error:]"
+ "-[IOKConnection callMethodWithSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:structOutput:structOutputSize:error:]"
+ "-[IOKConnection callMethodWithSelector:structInput:structInputSize:structOutput:structOutputSize:error:]"
+ "-[IOKConnection mapMemory64OfType:withOptions:atAddress:ofSize:error:]"
+ "-[IOKConnection setNotificationPort:ofType:withReference:error:]"
+ "-[IOKConnection setProperties:error:]"
+ "-[IOKConnection setProperty:withKey:error:]"
+ "-[IOKConnection trap:error:]"
+ "-[IOKConnection trap:p1:error:]"
+ "-[IOKConnection trap:p1:p2:error:]"
+ "-[IOKConnection trap:p1:p2:p3:error:]"
+ "-[IOKConnection trap:p1:p2:p3:p4:error:]"
+ "-[IOKConnection trap:p1:p2:p3:p4:p5:error:]"
+ "-[IOKConnection trap:p1:p2:p3:p4:p5:p6:error:]"
+ "-[IOKConnection unmapMemory64OfType:atAddress:error:]"
+ "IOKConnection %s failed with error 0x%08x"

```
