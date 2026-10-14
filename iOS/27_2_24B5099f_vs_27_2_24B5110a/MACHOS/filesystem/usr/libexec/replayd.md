## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-765.14.1.0.0
-  __TEXT.__text: 0xb9740
+765.15.2.0.0
+  __TEXT.__text: 0xb97a4
   __TEXT.__auth_stubs: 0x1920
   __TEXT.__objc_stubs: 0xf340
   __TEXT.__objc_methlist: 0x74b0
   __TEXT.__const: 0x3e4
   __TEXT.__gcc_except_tab: 0xfc8
-  __TEXT.__objc_methname: 0x15f73
-  __TEXT.__oslogstring: 0x167e9
-  __TEXT.__cstring: 0x17d0c
+  __TEXT.__objc_methname: 0x15f9b
+  __TEXT.__oslogstring: 0x16809
+  __TEXT.__cstring: 0x17d26
   __TEXT.__objc_classname: 0xa44
-  __TEXT.__objc_methtype: 0x43f5
+  __TEXT.__objc_methtype: 0x4410
   __TEXT.__unwind_info: 0x33e8
   __DATA_CONST.__const: 0x2b00
   __DATA_CONST.__cfstring: 0x5d40

   __DATA_CONST.__auth_got: 0xca0
   __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x11398
+  __DATA.__objc_const: 0x113b8
   __DATA.__objc_selrefs: 0x4728
-  __DATA.__objc_ivar: 0xd84
+  __DATA.__objc_ivar: 0xd88
   __DATA.__objc_data: 0x18b0
   __DATA.__data: 0xe54
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libobjc.A.dylib
   Functions: 3683
   Symbols:   802
-  CStrings:  7389
+  CStrings:  7391
 
Functions:
~ sub_100003548 : 384 -> 408
~ sub_1000036c8 -> sub_1000036e0 : 352 -> 376
~ sub_100005270 -> sub_1000052a0 : 248 -> 252
~ sub_100005368 -> sub_10000539c : 260 -> 264
~ sub_10000a730 -> sub_10000a768 : 144 -> 148
~ sub_10000ab9c -> sub_10000abd8 : 640 -> 668
~ sub_10000b4b8 -> sub_10000b510 : 128 -> 140
CStrings:
+ " [INFO] %{public}s:%d %p hasStarted=%d micDeviceUID=%@ micCaptureSessionCount=%ld"
+ " [INFO] %{public}s:%d didStart=%d pid=%d attributionSource=%ld micDeviceUID=%@"
+ "-[SCMediaAttributionManager updateMicrophoneCaptureDidStart:withAuditToken:micDeviceUID:]"
+ "-[SCMediaAttributionManager updateMicrophoneCaptureDidStart:withPID:attributionSource:micDeviceUID:]"
+ "_micDeviceUID"
+ "updateMicrophoneCaptureDidStart:withAuditToken:micDeviceUID:"
+ "updateMicrophoneCaptureDidStart:withPID:attributionSource:micDeviceUID:"
+ "v40@0:8B16i20q24@32"
+ "v60@0:8B16{?=[8I]}20@52"
- " [INFO] %{public}s:%d %p hasStarted=%d micCaptureSessionCount=%ld"
- " [INFO] %{public}s:%d didStart=%d pid=%d attributionSource=%ld"
- "-[SCMediaAttributionManager updateMicrophoneCaptureDidStart:withAuditToken:]"
- "-[SCMediaAttributionManager updateMicrophoneCaptureDidStart:withPID:attributionSource:]"
- "updateMicrophoneCaptureDidStart:withAuditToken:"
- "updateMicrophoneCaptureDidStart:withPID:attributionSource:"
- "v32@0:8B16i20q24"
```
