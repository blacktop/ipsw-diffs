## spinandd

> `/usr/libexec/spinandd`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-140.0.0.0.0
-  __TEXT.__text: 0x108fc
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x3ec
+142.0.0.0.0
+  __TEXT.__text: 0x10dc4
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x42c
   __TEXT.__const: 0x5e0
-  __TEXT.__objc_methname: 0xbe7
-  __TEXT.__cstring: 0x4059
+  __TEXT.__objc_methname: 0xcb6
+  __TEXT.__cstring: 0x40c2
   __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methtype: 0x3a4
-  __TEXT.__oslogstring: 0xbb5
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__objc_methtype: 0x3b3
+  __TEXT.__oslogstring: 0xcbe
+  __TEXT.__unwind_info: 0x370
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__const: 0x298
-  __DATA_CONST.__cfstring: 0x3c0
+  __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x4d0
-  __DATA.__objc_selrefs: 0x428
+  __DATA.__objc_selrefs: 0x480
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1c8

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 433
-  Symbols:   117
-  CStrings:  719
+  Functions: 446
+  Symbols:   126
+  CStrings:  740
 
Symbols:
+ _CFDataGetTypeID
+ _CFGetTypeID
+ _CFRelease
+ _CFStringGetTypeID
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ _IORegistryEntrySetCFProperty
+ _OBJC_CLASS_$_NSMutableString
+ _kCFAllocatorDefault
CStrings:
+ "%02x"
+ "142~377"
+ "Failed to open NVRAM options entry for read"
+ "Failed to open NVRAM options entry for write"
+ "Failed to write serial to NVRAM (0x%x)"
+ "Format status not fully loaded after format"
+ "IODeviceTree:/options"
+ "SPINANDFormat: on-flash Jrnl has newer minor than this build; not reformatting"
+ "SPINANDFormatAssert:message:"
+ "SPINANDMajorMismatchSeen"
+ "SPINANDNewerMinorSeen"
+ "SPINANDReadSerial"
+ "SPINANDWriteSerial:"
+ "allowReformat"
+ "allowReformat set; reformatting on format-status mismatch"
+ "appendFormat:"
+ "boolForKey:"
+ "copy"
+ "dataUsingEncoding:"
+ "initWithData:encoding:"
+ "spinandd-serial"
+ "stringWithCapacity:"
+ "v28@0:8B16r*20"
- "140~367"
- "serial"
```
