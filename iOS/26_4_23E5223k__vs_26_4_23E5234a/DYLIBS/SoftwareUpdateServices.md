## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.100.135.0.0
-  __TEXT.__text: 0xc3600
+950.102.1.0.0
+  __TEXT.__text: 0xc393c
   __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0xb4bc
+  __TEXT.__objc_methlist: 0xb4f4
   __TEXT.__const: 0x330
-  __TEXT.__cstring: 0x239bc
-  __TEXT.__gcc_except_tab: 0x12b8
+  __TEXT.__cstring: 0x23a03
+  __TEXT.__gcc_except_tab: 0x12c0
   __TEXT.__oslogstring: 0x85d
-  __TEXT.__unwind_info: 0x36a8
-  __TEXT.__objc_classname: 0xf77
-  __TEXT.__objc_methname: 0x1a3eb
+  __TEXT.__unwind_info: 0x36b0
+  __TEXT.__objc_classname: 0xf79
+  __TEXT.__objc_methname: 0x1a4e5
   __TEXT.__objc_methtype: 0x3502
-  __TEXT.__objc_stubs: 0x154a0
+  __TEXT.__objc_stubs: 0x15540
   __DATA_CONST.__got: 0xe08
   __DATA_CONST.__const: 0x2ab0
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6158
+  __DATA_CONST.__objc_selrefs: 0x6180
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x14d40
-  __AUTH_CONST.__objc_const: 0x16348
+  __AUTH_CONST.__cfstring: 0x14d80
+  __AUTH_CONST.__objc_const: 0x163a8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1018
-  __DATA.__objc_ivar: 0x9dc
+  __DATA.__objc_ivar: 0x9e4
   __DATA.__data: 0xef8
   __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0x1798

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 14A27B9A-29E1-3680-A019-27B5FF5378F6
-  Functions: 4693
-  Symbols:   15554
-  CStrings:  10880
+  UUID: 51E91239-CEC0-3040-BB76-B4F21F2D9F72
+  Functions: 4698
+  Symbols:   15571
+  CStrings:  10894
 
Symbols:
+ -[NSError(SUS) isNoMatchingUpdateFound]
+ -[SUScanner _filterDescriptor:forRequestedBuild:]
+ -[SUScanner _getDDMTargetUpdateWithPreferredDescriptor:alternateDescriptor:]
+ -[SUScanner ddmRequestedBuild]
+ -[SUScanner ddmRequestedPMV]
+ -[SUScanner setDdmRequestedBuild:]
+ -[SUScanner setDdmRequestedPMV:]
+ GCC_except_table87
+ _OBJC_IVAR_$_SUScanner._ddmRequestedBuild
+ _OBJC_IVAR_$_SUScanner._ddmRequestedPMV
+ _objc_msgSend$_filterDescriptor:forRequestedBuild:
+ _objc_msgSend$_getDDMTargetUpdateWithPreferredDescriptor:alternateDescriptor:
+ _objc_msgSend$ddmRequestedBuild
+ _objc_msgSend$ddmRequestedPMV
+ _objc_msgSend$isNoMatchingUpdateFound
+ _objc_msgSend$setDdmRequestedBuild:
+ _objc_msgSend$setDdmRequestedPMV:
- -[NSError(SUS) noMatchingUpdateFound]
- -[SUScanner _handleDescriptor:forRequestedBuild:]
- GCC_except_table86
- _objc_msgSend$_handleDescriptor:forRequestedBuild:
- _objc_msgSend$noMatchingUpdateFound
CStrings:
+ "%s: no requested build"
+ "%s: unexpected nil update descriptor"
+ "*"
+ "-[SUScanner _filterDescriptor:forRequestedBuild:]"
+ "Device is up-to-date; don't retry"
+ "T@\"NSString\",C,N,V_ddmRequestedBuild"
+ "T@\"NSString\",C,N,V_ddmRequestedPMV"
+ "_ddmRequestedBuild"
+ "_ddmRequestedPMV"
+ "_filterDescriptor:forRequestedBuild:"
+ "_getDDMTargetUpdateWithPreferredDescriptor:alternateDescriptor:"
+ "ddmRequestedBuild"
+ "ddmRequestedPMV"
+ "isNoMatchingUpdateFound"
+ "setDdmRequestedBuild:"
+ "setDdmRequestedPMV:"
- "%s: invalid parameters"
- "-[SUScanner _handleDescriptor:forRequestedBuild:]"
- "_handleDescriptor:forRequestedBuild:"
- "noMatchingUpdateFound"

```
