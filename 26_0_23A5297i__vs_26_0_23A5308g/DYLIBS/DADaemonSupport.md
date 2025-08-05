## DADaemonSupport

> `/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport`

```diff

-3796.11.0.0.0
-  __TEXT.__text: 0x1595c
+3799.0.0.0.0
+  __TEXT.__text: 0x159b8
   __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x1454
+  __TEXT.__objc_methlist: 0x145c
   __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0x600
   __TEXT.__oslogstring: 0x32e0
   __TEXT.__cstring: 0xce2
   __TEXT.__unwind_info: 0x510
   __TEXT.__objc_classname: 0x338
-  __TEXT.__objc_methname: 0x41c7
-  __TEXT.__objc_methtype: 0xb0d
+  __TEXT.__objc_methname: 0x41ed
+  __TEXT.__objc_methtype: 0xb28
   __TEXT.__objc_stubs: 0x30e0
   __DATA_CONST.__got: 0x358
   __DATA_CONST.__const: 0x428

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10d8
+  __DATA_CONST.__objc_selrefs: 0x10e0
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x4f0
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x1e08
+  __AUTH_CONST.__objc_const: 0x1e38
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_ivar: 0x144
   __DATA.__data: 0x3e8
   __DATA.__bss: 0x30
   __DATA.__common: 0x1

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4CBF638-B12A-3CC5-8B41-E35FC96FE7A6
-  Functions: 426
-  Symbols:   1851
-  CStrings:  1248
+  UUID: 0B9E9D19-5DC7-3468-BD88-C80B079EE8AB
+  Functions: 427
+  Symbols:   1854
+  CStrings:  1251
 
Symbols:
+ -[DATokenRegistrationRequest lock]
+ _OBJC_IVAR_$_DATokenRegistrationRequest._lock
Functions:
~ -[DATokenRegistrationRequest initWithToken:pushKey:wrapper:onBehalfOf:] : 204 -> 208
~ ___67-[DATokenRegistrationRequest URLSession:didBecomeInvalidWithError:]_block_invoke : 512 -> 536
~ ___67-[DATokenRegistrationRequest URLSession:task:didCompleteWithError:]_block_invoke : 512 -> 536
~ -[DATokenRegistrationRequest URLSession:dataTask:didReceiveResponse:completionHandler:] : 564 -> 580
~ -[DATokenRegistrationRequest sendRegistrationRequestForAccount:] : 1176 -> 1192
+ -[DATokenRegistrationRequest hsa2Session]
CStrings:
+ "T{os_unfair_lock_s=I},R,N,V_lock"
+ "lock"
+ "{os_unfair_lock_s=I}16@0:8"

```
