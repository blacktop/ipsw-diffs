## ICE

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ICE.framework/ICE`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2235.55.1.0.0
-  __TEXT.__text: 0x2d420
+2235.57.1.0.0
+  __TEXT.__text: 0x2d94c
   __TEXT.__objc_methlist: 0x3e4
   __TEXT.__const: 0x174
-  __TEXT.__cstring: 0x175b
-  __TEXT.__oslogstring: 0xc02e
-  __TEXT.__unwind_info: 0x358
+  __TEXT.__cstring: 0x1777
+  __TEXT.__oslogstring: 0xc37a
+  __TEXT.__unwind_info: 0x360
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x4e0
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x458
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x128
   __DATA.__bss: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 522
-  Symbols:   497
-  CStrings:  771
+  Functions: 529
+  Symbols:   502
+  CStrings:  775
 
Symbols:
+ _CCHmac
+ _ICEFreeRelayCandidatePairAllocsOnError
+ _MicroToMiddle32
+ _VCStunAuth_ValidateSTUNMessageIntegrity
+ _timingsafe_bcmp
CStrings:
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/ICE.subproj/Sources/ICEMessage.c:%d: MESSAGE_INTEGRITY validation failed in BINDING_REQUEST."
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/ICE.subproj/Sources/ICEMessage.c:%d: MESSAGE_INTEGRITY validation failed in BINDING_RESPONSE."
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/ICE.subproj/Sources/ICEMessage.c:%d: Missing MESSAGE_INTEGRITY in BINDING_REQUEST."
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/ICE.subproj/Sources/ICEMessage.c:%d: Missing MESSAGE_INTEGRITY in BINDING_RESPONSE."
+ " [%s] %s:%d Attempt to retain already released ICEList object %p"
+ "HRESULT ProcessBindingRequest(PICEINFO, PICELIST, PSTUNMSG, PIPPORT, double, const unsigned char *, int)"
- " [%s] %s:%d Attempt to retain already released ICEList object %x for call '%d'"
- "HRESULT ProcessBindingRequest(PICEINFO, PICELIST, PSTUNMSG, PIPPORT, double)"
```
