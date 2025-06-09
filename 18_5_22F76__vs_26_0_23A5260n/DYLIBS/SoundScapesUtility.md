## SoundScapesUtility

> `/System/Library/PrivateFrameworks/SoundScapesUtility.framework/SoundScapesUtility`

```diff

-155.50.5.0.0
-  __TEXT.__text: 0x1734
+202.0.0.0.0
+  __TEXT.__text: 0x186c
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x2d0
+  __TEXT.__objc_methlist: 0x320
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xf3
+  __TEXT.__cstring: 0xf4
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__oslogstring: 0xe9
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0xa4
-  __TEXT.__objc_methname: 0x9a8
-  __TEXT.__objc_methtype: 0x2f5
-  __TEXT.__objc_stubs: 0x9a0
+  __TEXT.__unwind_info: 0x108
+  __TEXT.__objc_classname: 0xbf
+  __TEXT.__objc_methname: 0xa1a
+  __TEXT.__objc_methtype: 0x30e
+  __TEXT.__objc_stubs: 0x9e0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x120
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x370
+  __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x4c0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x24
+  __AUTH_CONST.__objc_const: 0x5c0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x180
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 802A00EC-57C9-3D84-A341-CD32798D5DC6
-  Functions: 40
-  Symbols:   294
-  CStrings:  192
+  UUID: 1EA16D74-E8F6-327B-B66C-ED21F5503D26
+  Functions: 46
+  Symbols:   317
+  CStrings:  202
 
Symbols:
+ +[SSUSoundScapesPickerManager pickerForMediaProfiles:forDelegate:]
+ +[SSUSoundScapesPickerManager pickerForMediaProfiles:forDelegate:].cold.1
+ +[SSUSoundScapesPickerManager pickerSupportHome:targetMediaProfiles:]
+ -[SSUSoundScapesMediaProfile .cxx_destruct]
+ -[SSUSoundScapesMediaProfile backingAccessory]
+ -[SSUSoundScapesMediaProfile home]
+ -[SSUSoundScapesMediaProfile initWithAccessory:forHome:]
+ -[SSUSoundScapesMediaProfile setBackingAccessory:]
+ -[SSUSoundScapesMediaProfile setHome:]
+ GCC_except_table33
+ _OBJC_CLASS_$_SSUSoundScapesMediaProfile
+ _OBJC_IVAR_$_SSUSoundScapesMediaProfile._backingAccessory
+ _OBJC_IVAR_$_SSUSoundScapesMediaProfile._home
+ _OBJC_METACLASS_$_SSUSoundScapesMediaProfile
+ __OBJC_$_INSTANCE_METHODS_SSUSoundScapesMediaProfile
+ __OBJC_$_INSTANCE_VARIABLES_SSUSoundScapesMediaProfile
+ __OBJC_$_PROP_LIST_SSUSoundScapesMediaProfile
+ __OBJC_CLASS_RO_$_SSUSoundScapesMediaProfile
+ __OBJC_METACLASS_RO_$_SSUSoundScapesMediaProfile
+ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke.141
+ ___69+[SSUSoundScapesPickerManager pickerSupportHome:targetMediaProfiles:]_block_invoke
+ ___block_descriptor_32_e46_"NSString"16?0"SSUSoundScapesMediaProfile"8l
+ ___block_literal_global.118
+ ___block_literal_global.134
+ _objc_msgSend$backingAccessory
+ _objc_msgSend$home
+ _objc_msgSend$setBackingAccessory:
+ _objc_msgSend$setHome:
- +[SSUSoundScapesPickerManager pickerForMediaProfileContainers:forDelegate:]
- +[SSUSoundScapesPickerManager pickerForMediaProfileContainers:forDelegate:].cold.1
- +[SSUSoundScapesPickerManager pickerSupportHome:targetMediaProfileContainers:]
- GCC_except_table27
- ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke.121
- ___78+[SSUSoundScapesPickerManager pickerSupportHome:targetMediaProfileContainers:]_block_invoke
- ___block_descriptor_32_e45_"NSString"16?0"<HFMediaProfileContainer>"8l
- ___block_literal_global.114
- ___block_literal_global.98
- _objc_msgSend$hf_backingAccessory
- _objc_msgSend$hf_home
CStrings:
+ "@\"HMAccessory\""
+ "@\"HMHome\""
+ "@\"NSString\"16@?0@\"SSUSoundScapesMediaProfile\"8"
+ "SSUSoundScapesMediaProfile"
+ "T@\"HMAccessory\",W,V_backingAccessory"
+ "T@\"HMHome\",W,V_home"
+ "_backingAccessory"
+ "_home"
+ "backingAccessory"
+ "home"
+ "initWithAccessory:forHome:"
+ "pickerForMediaProfiles:forDelegate:"
+ "pickerSupportHome:targetMediaProfiles:"
+ "setBackingAccessory:"
+ "setHome:"
- "@\"NSString\"16@?0@\"<HFMediaProfileContainer>\"8"
- "hf_backingAccessory"
- "hf_home"
- "pickerForMediaProfileContainers:forDelegate:"
- "pickerSupportHome:targetMediaProfileContainers:"

```
