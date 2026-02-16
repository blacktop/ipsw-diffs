## SoundScapesUtility

> `/System/Library/PrivateFrameworks/SoundScapesUtility.framework/SoundScapesUtility`

```diff

-202.10.4.0.0
-  __TEXT.__text: 0x186c
-  __TEXT.__auth_stubs: 0x2e0
+202.40.8.0.0
+  __TEXT.__text: 0x19bc
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x320
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0xf4
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__oslogstring: 0xe9
-  __TEXT.__unwind_info: 0x108
+  __TEXT.__unwind_info: 0x110
   __TEXT.__objc_classname: 0xbf
   __TEXT.__objc_methname: 0xa1a
   __TEXT.__objc_methtype: 0x30e

   __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x180
+  __AUTH_CONST.__auth_got: 0x160
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x5c0

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2E12263F-7FED-3F21-84FA-6B7A49CBECC6
+  UUID: 5677EF4E-4070-37D9-8848-DC16AB1FFC03
   Functions: 46
-  Symbols:   317
+  Symbols:   313
   CStrings:  202
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ __SSULoggingFacility : 68 -> 84
~ -[SSUSoundScapesMediaProfile initWithAccessory:forHome:] : 140 -> 136
~ -[_SSUSoundScapesDelegateForwarder initForViewController:] : 516 -> 568
~ ___61-[_SSUSoundScapesDelegateForwarder mediaPickerConfirmChoices]_block_invoke : 84 -> 88
~ -[_SSUSoundScapesDelegateForwarder selectedSoundScapes:withError:] : 204 -> 192
~ ___50-[_SSUSoundScapesDelegateForwarder requestDismiss]_block_invoke : 76 -> 80
~ -[_SSUSoundScapesDelegateForwarder pickerDismissed] : 184 -> 200
~ ___43-[_SSUSoundScapesDelegateForwarder cleanup]_block_invoke : 68 -> 72
~ +[SSUSoundScapesPickerManager sharedManager] : 160 -> 176
~ -[SSUSoundScapesPickerManager init] : 144 -> 152
~ -[SSUSoundScapesPickerManager registerViewController:forMediaProfiles:andDelegate:] : 176 -> 172
~ +[SSUSoundScapesPickerManager pickerSupportHome:targetMediaProfiles:] : 80 -> 88
~ +[SSUSoundScapesPickerManager pickerIdentity] : 68 -> 84
~ ___45+[SSUSoundScapesPickerManager pickerIdentity]_block_invoke : 188 -> 200
~ +[SSUSoundScapesPickerManager pickerForMediaProfiles:forDelegate:] : 1116 -> 1216
~ -[SSUSoundScapesPickerManager hostViewControllerDidActivate:] : 996 -> 1056
~ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke : 104 -> 116
~ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke_2 : 244 -> 256
~ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke_3 : 100 -> 108
~ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke.141 : 120 -> 124
~ -[SSUSoundScapesPickerManager hostViewControllerWillDeactivate:error:] : 132 -> 136

```
