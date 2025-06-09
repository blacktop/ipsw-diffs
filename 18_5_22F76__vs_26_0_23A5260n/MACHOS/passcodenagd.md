## passcodenagd

> `/usr/libexec/passcodenagd`

```diff

-2400.5.2.0.0
-  __TEXT.__text: 0x25a8
+2420.1.1.0.0
+  __TEXT.__text: 0x2700
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x680
   __TEXT.__objc_methlist: 0xdc
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x32a
   __TEXT.__oslogstring: 0x5b4
   __TEXT.__objc_classname: 0x27
   __TEXT.__objc_methtype: 0x56
-  __TEXT.__objc_methname: 0x679
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__objc_methname: 0x739
+  __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__auth_got: 0x1c8
-  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x148
-  __DATA.__objc_selrefs: 0x178
+  __DATA.__objc_selrefs: 0x1a0
   __DATA.__objc_data: 0xa0
-  __DATA.__common: 0x3a
+  __DATA.__common: 0x32
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 586C08A4-D8B0-3E39-BD00-032B36A880A4
+  UUID: A31FCCB6-3541-3E72-A28B-CC9D439480BA
   Functions: 40
-  Symbols:   81
-  CStrings:  138
+  Symbols:   83
+  CStrings:  143
 
Symbols:
+ _OBJC_CLASS_$_MCExtractablePasscodeContextWrapper
+ _OBJC_CLASS_$_NSString
Functions:
~ sub_100001548 : 172 -> 156
~ sub_100001930 -> sub_100001920 : 1424 -> 1708
~ sub_100001ec0 -> sub_100001fcc : 424 -> 456
~ sub_100002ea4 -> sub_100002fd0 : 308 -> 352
CStrings:
+ "_newZStringWithString:"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:outError:"
+ "contextWrapperForExtractablePasscode:outError:"
+ "dictionaryWithObjects:forKeys:count:"
+ "externalizedContext"
+ "length"
+ "notifyCDPOfNewPasscodeWithContext:completion:"
+ "passcode"
+ "passcodeContext:meetsCurrentConstraintsOutError:"
+ "passcodeIsEqualToString:"
+ "unlockDeviceWithPasscodeContext:outError:"
+ "unlockScreenTypeForPasscodeContext:outSimplePasscodeType:"
- "changePasscodeFrom:to:outError:"
- "dictionaryWithObjectsAndKeys:"
- "isEqualToString:"
- "notifyCDPThatPasscodeChangedTo:completion:"
- "passcode:meetsCurrentConstraintsOutError:"
- "unlockDeviceWithPasscode:outError:"
- "unlockScreenTypeForPasscode:outSimplePasscodeType:"

```
