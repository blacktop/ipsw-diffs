## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-3186.0.12.0.0
-  __TEXT.__text: 0x3c6268
-  __TEXT.__objc_methlist: 0xd964
+3186.0.17.0.1
+  __TEXT.__text: 0x3c73bc
+  __TEXT.__objc_methlist: 0xd994
   __TEXT.__const: 0xcd60
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e

   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__oslogstring: 0x2f779
-  __TEXT.__cstring: 0x477f3
+  __TEXT.__oslogstring: 0x2fcb7
+  __TEXT.__cstring: 0x47a46
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__gcc_except_tab: 0xd4d0
-  __TEXT.__unwind_info: 0xd0e0
+  __TEXT.__gcc_except_tab: 0xd4dc
+  __TEXT.__unwind_info: 0xd0d8
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3d68
+  __DATA_CONST.__const: 0x3d20
   __DATA_CONST.__objc_classlist: 0x8e0
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x56f8
+  __DATA_CONST.__objc_selrefs: 0x5718
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x7c8
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__got: 0x828
   __AUTH_CONST.__const: 0x158b8
   __AUTH_CONST.__cfstring: 0x13d20
-  __AUTH_CONST.__objc_const: 0x1dd88
+  __AUTH_CONST.__objc_const: 0x1dd68
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__auth_got: 0x14c0
-  __AUTH.__objc_data: 0x42e0
+  __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x17bc
-  __DATA.__data: 0xe18
+  __DATA.__objc_ivar: 0x17b8
+  __DATA.__data: 0xe10
   __DATA.__common: 0x128
   __DATA_DIRTY.__objc_ivar: 0x1c0
-  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA_DIRTY.__objc_data: 0x55a0
   __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__common: 0x89
   __DATA_DIRTY.__bss: 0x10e0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12714
+  Functions: 12716
   Symbols:   1815
-  CStrings:  11413
+  CStrings:  11438
 
CStrings:
+ "-[CMDeviceStateManager simulateDeviceStateEventForPropertyA:propertyA0:propertyA1:propertyB:propertyC:propertyD:delaySecs:]"
+ "-[CMDeviceStateManagerInternal feedDeviceStateEvent:propertyA0Type:propertyA1Type:propertyBType:propertyCType:propertyDType:timestamp:continuousTimestamp:timestampAPArrivalSecs:]"
+ "-[CMDeviceStateManagerInternal sendEventToClientPrivate]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Framework/CoreMotion/DeviceState/CMDeviceStateManager.mm"
+ "Dropping event after teardown in onDeviceStateData:."
+ "Invalid simulated propertyA value"
+ "Invalid simulated propertyA0 value"
+ "Invalid simulated propertyA1 value"
+ "Invalid simulated propertyB value"
+ "Invalid simulated propertyC value"
+ "Invalid simulated propertyD value"
+ "No internal state, ignoring onNotification."
+ "No internal state, skipping teardown."
+ "No internal state; ignoring startUpdatesPrivateToQueue:withHandler:"
+ "No internal state; ignoring startUpdatesToQueue:withHandler:"
+ "[CMDeviceStateEvent isValidPropertyA:propertyA0]"
+ "[CMDeviceStateEvent isValidPropertyA:propertyA1]"
+ "[CMDeviceStateEvent isValidPropertyA:propertyA]"
+ "[CMDeviceStateEvent isValidPropertyB:propertyB]"
+ "[CMDeviceStateEvent isValidPropertyC:propertyC]"
+ "[CMDeviceStateEvent isValidPropertyD:propertyD]"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyA value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyA0 value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyA1 value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyB value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyC value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyD value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "-[CMDeviceStateManager feedDeviceStateEvent:propertyA0Type:propertyA1Type:propertyBType:propertyCType:propertyDType:timestamp:continuousTimestamp:timestampAPArrivalSecs:]_block_invoke"
- "-[CMDeviceStateManager sendEventToClientPrivate]"
```
