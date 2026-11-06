## afktool

> `/usr/bin/afktool`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-743.0.5.0.1
-  __TEXT.__text: 0x8944
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x800
-  __TEXT.__gcc_except_tab: 0x1008
-  __TEXT.__cstring: 0xf9f
-  __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0x2d
-  __TEXT.__objc_methname: 0x5a2
-  __TEXT.__unwind_info: 0x370
-  __DATA_CONST.__const: 0x2f0
-  __DATA_CONST.__cfstring: 0xa80
+743.40.4.0.0
+  __TEXT.__text: 0x7e50
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0x7c0
+  __TEXT.__gcc_except_tab: 0xf88
+  __TEXT.__cstring: 0xff5
+  __TEXT.__const: 0x28
+  __TEXT.__oslogstring: 0x3
+  __TEXT.__objc_methname: 0x55f
+  __TEXT.__unwind_info: 0x338
+  __DATA_CONST.__const: 0x290
+  __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0x148
-  __DATA.__objc_selrefs: 0x200
+  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__got: 0x120
+  __DATA.__objc_selrefs: 0x1f0
   __DATA.__data: 0x10
   __DATA.__common: 0x8
   __DATA.__bss: 0x1

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 100
-  Symbols:   153
-  CStrings:  233
+  Functions: 93
+  Symbols:   134
+  CStrings:  231
 
Symbols:
+ _AFKUserRegistryFromSerializedServices
+ _IOCFUnserializeBinary
+ _kAFKEventCancel
- _CFArrayAppendValue
- _CFArrayCreateMutable
- _CFDataCreate
- _CFDictionaryCreateMutable
- _CFDictionarySetValue
- _CFNumberCreate
- _CFRelease
- _CFRetain
- _CFSetAddValue
- _CFSetCreateMutable
- _CFStringCreateWithBytes
- _IOCFUnserializeWithSize
- __os_log_fault_impl
- _kCFBooleanFalse
- _kCFBooleanTrue
- _kCFTypeArrayCallBacks
- _kCFTypeDictionaryKeyCallBacks
- _kCFTypeDictionaryValueCallBacks
- _kCFTypeSetCallBacks
- _malloc_type_calloc
- _objc_storeStrong
- _syslog$DARWIN_EXTSN
CStrings:
+ "AppleFirmwareKit ToolvRC_ProjectBuildVersion Oct  3 2026 15:36:50"
+ "Could not build a registry from the captured services"
+ "Could not open an AFK Endpoint Interface"
+ "ERROR! Unserialize registry dump for service:0x%llx type:%@"
+ "Registry dump did not unserialize to a dictionary"
+ "setEventHandler:"
+ "v32@?0@\"AFKEndpointInterface\"8@\"NSString\"16@24"
- "0x%llx: AFKIOCFUnserializeWithSize failed"
- "AFKRootService"
- "AppleFirmwareKit ToolvRC_ProjectBuildVersion Aug  8 2026 15:17:26"
- "ERROR! Unserialize registry dump for service:0x%llx error:%@"
- "FIXME: IOUnserialize has detected a string that is not valid UTF-8, \"%s\"."
- "enumerateObjectsUsingBlock:"
- "objectAtIndexedSubscript:"
- "setObject:atIndexedSubscript:"
- "v32@?0@8Q16^B24"
```
