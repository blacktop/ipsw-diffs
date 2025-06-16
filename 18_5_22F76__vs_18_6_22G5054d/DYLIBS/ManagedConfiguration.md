## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2400.5.2.0.0
-  __TEXT.__text: 0xe0508
+2400.5.6.0.0
+  __TEXT.__text: 0xe1500
   __TEXT.__auth_stubs: 0x1690
-  __TEXT.__objc_methlist: 0xaca4
+  __TEXT.__objc_methlist: 0xad5c
   __TEXT.__const: 0x1124
-  __TEXT.__cstring: 0x16011
+  __TEXT.__cstring: 0x1603d
   __TEXT.__oslogstring: 0x8582
   __TEXT.__gcc_except_tab: 0xf6c
   __TEXT.__ustring: 0x50
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x2d00
+  __TEXT.__unwind_info: 0x2d58
   __TEXT.__objc_classname: 0xc51
-  __TEXT.__objc_methname: 0x1cc68
-  __TEXT.__objc_methtype: 0x2149
-  __TEXT.__objc_stubs: 0xd400
+  __TEXT.__objc_methname: 0x1ce49
+  __TEXT.__objc_methtype: 0x2164
+  __TEXT.__objc_stubs: 0xd460
   __DATA_CONST.__got: 0xa48
-  __DATA_CONST.__const: 0x4c78
+  __DATA_CONST.__const: 0x4c80
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x59c8
+  __DATA_CONST.__objc_selrefs: 0x5a10
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0xb58
-  __AUTH_CONST.__const: 0x2250
-  __AUTH_CONST.__cfstring: 0x191c0
-  __AUTH_CONST.__objc_const: 0xd400
+  __AUTH_CONST.__const: 0x22b0
+  __AUTH_CONST.__cfstring: 0x19200
+  __AUTH_CONST.__objc_const: 0xd430
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0x968
+  __DATA.__objc_ivar: 0x96c
   __DATA.__data: 0xb68
-  __DATA.__bss: 0xc99
+  __DATA.__bss: 0xcc9
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__bss: 0x218

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9501F43-F86C-3821-9AA1-4225953BA7CE
-  Functions: 5118
-  Symbols:   16428
-  CStrings:  11813
+  UUID: 41C6758D-253C-3686-9DAD-B3ED10409E55
+  Functions: 5149
+  Symbols:   16500
+  CStrings:  11829
 
Symbols:
+ -[MCProfileConnection(Misc) isAccessibilityTypingFeedbackAllowed]
+ -[MCProfileConnection(Misc) setAutoCorrectionAllowed:completion:]
+ -[MCProfileConnection(Misc) setContinuousPathKeyboardAllowed:completion:]
+ -[MCProfileConnection(Misc) setKeyboardShortcutsAllowed:completion:]
+ -[MCProfileConnection(Misc) setPredictiveKeyboardAllowed:completion:]
+ -[MCProfileConnection(Misc) setSmartPunctuationAllowed:completion:]
+ -[MCProfileConnection(Misc) setSpellCheckAllowed:completion:]
+ -[MCProfileConnection(Settings) setBoolValue:forSetting:completion:]
+ -[MCProfileConnection(Settings) setValue:forSetting:completion:]
+ -[MCProfileConnection(Settings) setValues:forIntersectionSetting:completion:]
+ -[MCProfileConnection(Settings) setValues:forIntersectionSetting:toSystem:user:waitUntilCompleted:completion:]
+ -[MCProfileConnection(Settings) setValues:forUnionSetting:completion:]
+ -[MCProfileConnection(Settings) setValues:forUnionSetting:toSystem:user:waitUntilCompleted:completion:]
+ -[MCSingleAppModeConfiguration allowAccessibilityTypingFeedback]
+ -[MCSingleAppModeConfiguration setAllowAccessibilityTypingFeedback:]
+ GCC_except_table278
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table97
+ _MCConfigurationProfilesSystemGroupContainerNF
+ _MCFeatureAccessibilityTypingFeedbackAllowed
+ _MCPostSetupAutoInstallProfilePathNF
+ _MCPostSetupAutoInstallProfilePathNF.cold.1
+ _MCPostSetupAutoInstallProfilePathNF.once
+ _MCPostSetupAutoInstallProfilePathNF.str
+ _MCSystemProfileLibraryDirectoryNF
+ _MCSystemProfileLibraryDirectoryNF.cold.1
+ _MCSystemProfileLibraryDirectoryNF.once
+ _MCSystemProfileLibraryDirectoryNF.str
+ _MCSystemProfileStorageDirectoryNF
+ _MCSystemProfileStorageDirectoryNF.cold.1
+ _MCSystemProfileStorageDirectoryNF.once
+ _MCSystemProfileStorageDirectoryNF.str
+ _OBJC_IVAR_$_MCSingleAppModeConfiguration._allowAccessibilityTypingFeedback
+ ___61-[MCProfileConnection(Misc) setSpellCheckAllowed:completion:]_block_invoke
+ ___65-[MCProfileConnection(Misc) setAutoCorrectionAllowed:completion:]_block_invoke
+ ___67-[MCProfileConnection(Misc) setSmartPunctuationAllowed:completion:]_block_invoke
+ ___68-[MCProfileConnection(Misc) setKeyboardShortcutsAllowed:completion:]_block_invoke
+ ___69-[MCProfileConnection(Misc) setPredictiveKeyboardAllowed:completion:]_block_invoke
+ ___73-[MCProfileConnection(Misc) setContinuousPathKeyboardAllowed:completion:]_block_invoke
+ ___MCPostSetupAutoInstallProfilePathNF_block_invoke
+ ___MCSystemProfileLibraryDirectoryNF_block_invoke
+ ___MCSystemProfileStorageDirectoryNF_block_invoke
+ ___block_literal_global.103
+ ___block_literal_global.107
+ ___block_literal_global.112
+ ___block_literal_global.117
+ ___block_literal_global.124
+ ___block_literal_global.129
+ ___block_literal_global.136
+ ___block_literal_global.141
+ ___block_literal_global.146
+ ___block_literal_global.151
+ ___block_literal_global.156
+ ___block_literal_global.161
+ ___block_literal_global.166
+ ___block_literal_global.171
+ ___block_literal_global.176
+ ___block_literal_global.181
+ ___block_literal_global.186
+ ___block_literal_global.191
+ ___block_literal_global.193
+ ___block_literal_global.198
+ ___block_literal_global.203
+ ___block_literal_global.208
+ ___block_literal_global.216
+ ___block_literal_global.221
+ ___block_literal_global.226
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.242
+ ___block_literal_global.63
+ ___block_literal_global.73
+ ___block_literal_global.78
+ ___block_literal_global.88
+ _objc_msgSend$allowAccessibilityTypingFeedback
+ _objc_msgSend$setValue:forSetting:passcode:completion:
+ _objc_msgSend$setValues:forIntersectionSetting:toSystem:user:waitUntilCompleted:completion:
+ _objc_msgSend$setValues:forUnionSetting:toSystem:user:waitUntilCompleted:completion:
- GCC_except_table265
- ___block_literal_global.100
- ___block_literal_global.115
- ___block_literal_global.120
- ___block_literal_global.127
- ___block_literal_global.132
- ___block_literal_global.137
- ___block_literal_global.142
- ___block_literal_global.162
- ___block_literal_global.167
- ___block_literal_global.172
- ___block_literal_global.177
- ___block_literal_global.182
- ___block_literal_global.184
- ___block_literal_global.189
- ___block_literal_global.194
- ___block_literal_global.199
- ___block_literal_global.207
- ___block_literal_global.212
- ___block_literal_global.217
- ___block_literal_global.222
- ___block_literal_global.227
- ___block_literal_global.229
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.237
- ___block_literal_global.239
- ___block_literal_global.253
- ___block_literal_global.258
- ___block_literal_global.263
- ___block_literal_global.61
- ___block_literal_global.71
- ___block_literal_global.76
- ___block_literal_global.81
- ___block_literal_global.86
- ___block_literal_global.91
- ___block_literal_global.96
- _objc_msgSend$setParametersForSettingsByType:toSystem:user:
CStrings:
+ "/.nofollow"
+ "TB,N,V_allowAccessibilityTypingFeedback"
+ "_allowAccessibilityTypingFeedback"
+ "allowAccessibilityTypingFeedback"
+ "isAccessibilityTypingFeedbackAllowed"
+ "setAllowAccessibilityTypingFeedback:"
+ "setBoolValue:forSetting:completion:"
+ "setValue:forSetting:completion:"
+ "setValues:forIntersectionSetting:completion:"
+ "setValues:forIntersectionSetting:toSystem:user:waitUntilCompleted:completion:"
+ "setValues:forUnionSetting:completion:"
+ "setValues:forUnionSetting:toSystem:user:waitUntilCompleted:completion:"
+ "v52@0:8@16@24B32B36B40@?44"

```
