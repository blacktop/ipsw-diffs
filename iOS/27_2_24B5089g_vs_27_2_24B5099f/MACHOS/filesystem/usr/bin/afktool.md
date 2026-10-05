## afktool

> `/usr/bin/afktool`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-743.40.3.0.0
-  __TEXT.__text: 0x8284
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x800
-  __TEXT.__gcc_except_tab: 0x1004
-  __TEXT.__cstring: 0xf9f
-  __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0x2d
-  __TEXT.__objc_methname: 0x5a2
-  __TEXT.__unwind_info: 0x348
-  __DATA_CONST.__const: 0x2a0
-  __DATA_CONST.__cfstring: 0xa80
+743.40.4.0.0
+  __TEXT.__text: 0x7838
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x7c0
+  __TEXT.__gcc_except_tab: 0xf84
+  __TEXT.__cstring: 0xff5
+  __TEXT.__const: 0x28
+  __TEXT.__oslogstring: 0x3
+  __TEXT.__objc_methname: 0x55f
+  __TEXT.__unwind_info: 0x318
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0x148
-  __DATA.__objc_selrefs: 0x200
+  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__got: 0x120
+  __DATA.__objc_selrefs: 0x1f0
   __DATA.__data: 0x10
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 86
-  Symbols:   176
-  CStrings:  233
+  Functions: 81
+  Symbols:   157
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
- _syslog
CStrings:
+ "AppleFirmwareKit ToolvRC_ProjectBuildVersion Sep 27 2026 20:36:23"
+ "Could not build a registry from the captured services"
+ "Could not open an AFK Endpoint Interface"
+ "ERROR! Unserialize registry dump for service:0x%llx type:%@"
+ "Registry dump did not unserialize to a dictionary"
+ "setEventHandler:"
+ "v32@?0@\"AFKEndpointInterface\"8@\"NSString\"16@24"
- "0x%llx: AFKIOCFUnserializeWithSize failed"
- "AFKRootService"
- "AppleFirmwareKit ToolvRC_ProjectBuildVersion Sep 12 2026 04:49:29"
- "ERROR! Unserialize registry dump for service:0x%llx error:%@"
- "FIXME: IOUnserialize has detected a string that is not valid UTF-8, \"%s\"."
- "enumerateObjectsUsingBlock:"
- "objectAtIndexedSubscript:"
- "setObject:atIndexedSubscript:"
- "v32@?0@8Q16^B24"
```
