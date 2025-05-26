## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-3.26.6.4.0
-  __TEXT.__text: 0x3f5b4
+3.26.6.8.0
+  __TEXT.__text: 0x3f2f4
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x505c
+  __TEXT.__objc_methlist: 0x503c
   __TEXT.__const: 0x188
   __TEXT.__oslogstring: 0x15a8
-  __TEXT.__cstring: 0x2602
+  __TEXT.__cstring: 0x25dd
   __TEXT.__gcc_except_tab: 0x51c
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x1160
+  __TEXT.__unwind_info: 0x1158
   __TEXT.__objc_classname: 0x10b5
-  __TEXT.__objc_methname: 0x11f41
-  __TEXT.__objc_methtype: 0x4497
-  __TEXT.__objc_stubs: 0xbe60
+  __TEXT.__objc_methname: 0x11e37
+  __TEXT.__objc_methtype: 0x4483
+  __TEXT.__objc_stubs: 0xbd60
   __DATA_CONST.__got: 0x518
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x106e0
-  __DATA_CONST.__objc_selrefs: 0x3a08
+  __DATA_CONST.__objc_const: 0x10680
+  __DATA_CONST.__objc_selrefs: 0x39c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x7c8
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__objc_const: 0x23c0
-  __AUTH_CONST.__cfstring: 0x2a60
+  __AUTH_CONST.__cfstring: 0x2a20
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x3e8
   __AUTH.__objc_data: 0x1c20
-  __DATA.__objc_ivar: 0x560
+  __DATA.__objc_ivar: 0x558
   __DATA.__data: 0x11a8
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1824
-  Symbols:   7291
-  CStrings:  3855
+  Functions: 1821
+  Symbols:   7275
+  CStrings:  3840
 
Symbols:
+ +[DMCProfileViewModel trustTextForProfile:]
+ -[DMCProfileItemDetail initWithTitle:detail:trustText:]
+ _objc_msgSend$initWithTitle:detail:trustText:
+ _objc_msgSend$trustTextForProfile:
- +[DMCProfileViewModel trustTextForProfile:outIsTrusted:]
- -[DMCProfileItemDetail initWithTitle:detail:isTrusted:trustText:]
- -[DMCProfileItemDetail isTrusted]
- -[DMCProfileKeyValueView setVerifiedImageView:]
- -[DMCProfileKeyValueView verifiedImageView]
- _OBJC_IVAR_$_DMCProfileItemDetail._isTrusted
- _OBJC_IVAR_$_DMCProfileKeyValueView._verifiedImageView
- _objc_msgSend$DMCProfileVerifiedColor
- _objc_msgSend$configurationWithFont:
- _objc_msgSend$image
- _objc_msgSend$imageWithRenderingMode:
- _objc_msgSend$initWithTitle:detail:isTrusted:trustText:
- _objc_msgSend$isTrusted
- _objc_msgSend$setTintColor:
- _objc_msgSend$systemImageNamed:withConfiguration:
- _objc_msgSend$trustTextForProfile:outIsTrusted:
- _objc_msgSend$verifiedImageView
CStrings:
+ "initWithTitle:detail:trustText:"
+ "trustTextForProfile:"
- "@44@0:8@16@24B32@36"
- "DMC_PROFILE_TRUST_VERIFIED"
- "T@\"UIImageView\",&,N,V_verifiedImageView"
- "TB,R,N,V_isTrusted"
- "_isTrusted"
- "_verifiedImageView"
- "checkmark"
- "configurationWithFont:"
- "image"
- "imageWithRenderingMode:"
- "initWithTitle:detail:isTrusted:trustText:"
- "isTrusted"
- "setTintColor:"
- "setVerifiedImageView:"
- "systemImageNamed:withConfiguration:"
- "trustTextForProfile:outIsTrusted:"
- "verifiedImageView"

```
