## ANEServices

> `/System/Library/PrivateFrameworks/ANEServices.framework/ANEServices`

```diff

-8.300.0.0.0
-  __TEXT.__text: 0x23b24
-  __TEXT.__auth_stubs: 0xd10
+8.508.0.0.0
+  __TEXT.__text: 0x25540
+  __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0x2b1
-  __TEXT.__cstring: 0x1c1c
-  __TEXT.__gcc_except_tab: 0xf54
-  __TEXT.__oslogstring: 0x231c
-  __TEXT.__unwind_info: 0x848
-  __TEXT.__objc_classname: 0xf
+  __TEXT.__const: 0x2e9
+  __TEXT.__cstring: 0x1c76
+  __TEXT.__gcc_except_tab: 0x1000
+  __TEXT.__oslogstring: 0x25b2
+  __TEXT.__unwind_info: 0x800
+  __TEXT.__objc_classname: 0x10
   __TEXT.__objc_methname: 0x27
   __TEXT.__objc_methtype: 0x8
   __TEXT.__objc_stubs: 0x80
   __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x430
+  __DATA_CONST.__const: 0x480
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__const: 0x150
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x90
-  __DATA.__data: 0x10
-  __DATA.__bss: 0x11
+  __DATA.__data: 0x50
+  __DATA.__bss: 0x20
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 631
-  Symbols:   933
-  CStrings:  509
+  Functions: 616
+  Symbols:   959
+  CStrings:  531
 
Symbols:
+ _CFRunLoopPerformBlock
+ _CFRunLoopSourceCreate
+ _CFRunLoopWakeUp
+ _H11ANEProgramChainingSetActiveProcedure
+ _H11ANESessionHintRequest
+ __Block_object_dispose
+ __ZN6H11ANE12H11ANEDevice18ANE_GetClientsInfoEP23H11ANEClientsInfoStruct
+ __ZN6H11ANE12H11ANEDevice21ANE_GetDriverPropertyE17ANEDriverPropertyPj
+ __ZN6H11ANE12H11ANEDevice21ANE_SetDriverPropertyE17ANEDriverPropertyj
+ __ZN6H11ANE12H11ANEDevice22ANE_SessionHintRequestEP27H11ANESessionHintArgsStructP29H11ANESessionHintOutputStruct
+ __ZN6H11ANE12H11ANEDevice37ANE_ProgramChainingSetActiveProcedureEP44H11ANEChainingSetActiveProcedureParamsStruct
+ __ZN6H11ANE31H11ANEEnableSharedServiceThreadEv
+ _malloc_type_calloc
+ _strerror
- __ZN6H11ANE12H11ANEDevice25ANE_GetDriverLoggingFlagsEPj
- __ZN6H11ANE12H11ANEDevice25ANE_SetDriverLoggingFlagsEj
CStrings:
+ "%s: failed to create run loop source\n"
+ "Detached from shared service thread\n"
+ "ERROR: %s: Bad arguments pANEDevice=0x%p chainingActiveParams=%p\n"
+ "H11ANEDeviceSessionHintRequest"
+ "H11ANEProgramChainingSetActiveProcedure"
+ "H11ANESessionHintRequest"
+ "No shared service thread\n"
+ "No shared service thread to release\n"
+ "ServicesSessionHintRequest"
+ "SharedServiceThreadStart"
+ "attaching to shared service thread\n"
+ "creating shared service thread\n"
+ "failed to allocate shared service thread struct\n"
+ "failed to init shared service thread\n"
+ "hint=%u handle=0x%llx"
+ "pthread_attr_init: %s\n"
+ "pthread_attr_setdetachstate: %s\n"
+ "pthread_attr_setschedparam: %s\n"
+ "pthread_create: %s\n"
+ "shared service thread exit\n"
+ "shared service thread release: refCount=%u\n"
+ "shared service thread retain: refCount=%u\n"

```
