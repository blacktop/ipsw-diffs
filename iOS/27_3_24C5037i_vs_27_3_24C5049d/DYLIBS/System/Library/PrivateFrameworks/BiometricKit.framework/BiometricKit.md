## BiometricKit

> `/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`

```diff

-578.60.5.0.4
-  __TEXT.__text: 0x3bf04
-  __TEXT.__objc_methlist: 0x2d24
-  __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x2841
-  __TEXT.__oslogstring: 0x4fee
+578.60.14.0.2
+  __TEXT.__text: 0x3df5c
+  __TEXT.__objc_methlist: 0x2e14
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x2a4f
+  __TEXT.__oslogstring: 0x5494
   __TEXT.__gcc_except_tab: 0xba0
-  __TEXT.__unwind_info: 0x1658
+  __TEXT.__unwind_info: 0x16e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x848
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1780
+  __DATA_CONST.__objc_selrefs: 0x17a8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x120
-  __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__got: 0x248
-  __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x1800
-  __AUTH_CONST.__objc_const: 0x5280
+  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_arraydata: 0x70
+  __DATA_CONST.__got: 0x278
+  __AUTH_CONST.__const: 0x5e0
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x54f8
   __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x3d0
-  __DATA.__objc_ivar: 0x2f0
-  __DATA.__data: 0x2a0
-  __DATA_DIRTY.__objc_data: 0xe60
+  __AUTH_CONST.__auth_got: 0x418
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x2fc
+  __DATA.__data: 0x2a8
+  __DATA_DIRTY.__objc_data: 0xeb0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1555
-  Symbols:   2095
-  CStrings:  745
+  Functions: 1597
+  Symbols:   2166
+  CStrings:  780
 
Symbols:
+ +[BKDeviceConvenience deviceAvailableWithFailure:]
+ -[BKDeviceConvenience bioLockoutState:forUser:error:]
+ -[BKDeviceConvenience createMatchOperationWithError:]
+ -[BKDeviceConvenience extendedBioLockoutState:forUser:error:]
+ -[BKDeviceConvenience identitiesForUser:error:]
+ -[BKDeviceConvenience identitiesWithError:]
+ -[BKDeviceConvenience init]
+ -[BKDeviceConvenience prewarmWithError:]
+ -[BKMatchConvenienceOperation cameraType]
+ -[BKMatchConvenienceOperation enableAutoRetry:error:]
+ -[BKMatchConvenienceOperation identityUpdateOnly]
+ -[BKMatchConvenienceOperation initWithDevice:]
+ -[BKMatchConvenienceOperation optionsDictionaryWithError:]
+ -[BKMatchConvenienceOperation setCameraType:]
+ -[BKMatchConvenienceOperation setIdentityUpdateOnly:]
+ -[BKMatchConvenienceOperation setShouldAutoRetry:]
+ -[BKMatchConvenienceOperation shouldAutoRetry]
+ GCC_except_table100
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table127
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table146
+ GCC_except_table149
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table170
+ GCC_except_table173
+ GCC_except_table179
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table194
+ GCC_except_table197
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table209
+ GCC_except_table212
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table224
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table242
+ GCC_except_table250
+ GCC_except_table255
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table264
+ GCC_except_table267
+ GCC_except_table270
+ GCC_except_table273
+ GCC_except_table276
+ GCC_except_table279
+ GCC_except_table282
+ GCC_except_table39
+ GCC_except_table42
+ GCC_except_table47
+ GCC_except_table97
+ _CFDictionaryGetValue
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _MGIsDeviceOfType
+ _OBJC_CLASS_$_BKDeviceConvenience
+ _OBJC_CLASS_$_BKMatchConvenienceOperation
+ _OBJC_CLASS_$_BKMatchConvenienceResultInfo
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_IVAR_$_BKMatchConvenienceOperation._cameraType
+ _OBJC_IVAR_$_BKMatchConvenienceOperation._identityUpdateOnly
+ _OBJC_IVAR_$_BKMatchConvenienceOperation._shouldAutoRetry
+ _OBJC_METACLASS_$_BKDeviceConvenience
+ _OBJC_METACLASS_$_BKMatchConvenienceOperation
+ _OBJC_METACLASS_$_BKMatchConvenienceResultInfo
+ __OBJC_$_CLASS_METHODS_BKDeviceConvenience
+ __OBJC_$_INSTANCE_METHODS_BKDeviceConvenience
+ __OBJC_$_INSTANCE_METHODS_BKMatchConvenienceOperation
+ __OBJC_$_INSTANCE_VARIABLES_BKMatchConvenienceOperation
+ __OBJC_$_PROP_LIST_BKDeviceConvenience
+ __OBJC_$_PROP_LIST_BKMatchConvenienceOperation
+ __OBJC_CLASS_RO_$_BKDeviceConvenience
+ __OBJC_CLASS_RO_$_BKMatchConvenienceOperation
+ __OBJC_CLASS_RO_$_BKMatchConvenienceResultInfo
+ __OBJC_METACLASS_RO_$_BKDeviceConvenience
+ __OBJC_METACLASS_RO_$_BKMatchConvenienceOperation
+ __OBJC_METACLASS_RO_$_BKMatchConvenienceResultInfo
+ ___60+[BiometricKitXPCClientConnection connectionWithDeviceType:]_block_invoke_3
+ ___NSArray0__struct
+ ___isBioConvenienceClientAllowed_block_invoke
+ ___isBioConvenienceDisabledInAKS_block_invoke
+ ___isBioConvenienceDisabledInAKS_block_invoke_2
+ ___isBioConvenienceDisabledInAKS_block_invoke_3
+ ___isBioConveniencePlatform_block_invoke
+ __xpc_type_bool
+ _aks_get_configuration
+ _connectionWithDeviceType:.convenienceConnection
+ _isBioConvenienceClientAllowed
+ _isBioConvenienceClientAllowed.clientAllowed
+ _isBioConvenienceClientAllowed.onceToken
+ _isBioConvenienceDisabledInAKS.createdNotifyToken
+ _isBioConvenienceDisabledInAKS.disabled
+ _isBioConvenienceDisabledInAKS.onceToken
+ _isBioConvenienceDisabledInAKS.unavailableNotifyToken
+ _isBioConveniencePlatform
+ _isBioConveniencePlatform.bioConveniencePlatform
+ _isBioConveniencePlatform.onceToken
+ _kAKSConfigFlags
+ _xpc_bool_get_value
+ _xpc_copy_entitlement_for_self
+ _xpc_get_type
- GCC_except_table102
- GCC_except_table105
- GCC_except_table108
- GCC_except_table114
- GCC_except_table117
- GCC_except_table120
- GCC_except_table123
- GCC_except_table126
- GCC_except_table139
- GCC_except_table142
- GCC_except_table145
- GCC_except_table148
- GCC_except_table151
- GCC_except_table154
- GCC_except_table160
- GCC_except_table163
- GCC_except_table166
- GCC_except_table169
- GCC_except_table172
- GCC_except_table178
- GCC_except_table181
- GCC_except_table184
- GCC_except_table187
- GCC_except_table190
- GCC_except_table193
- GCC_except_table196
- GCC_except_table202
- GCC_except_table205
- GCC_except_table208
- GCC_except_table211
- GCC_except_table214
- GCC_except_table217
- GCC_except_table220
- GCC_except_table223
- GCC_except_table226
- GCC_except_table229
- GCC_except_table232
- GCC_except_table235
- GCC_except_table238
- GCC_except_table241
- GCC_except_table249
- GCC_except_table254
- GCC_except_table257
- GCC_except_table260
- GCC_except_table263
- GCC_except_table266
- GCC_except_table269
- GCC_except_table272
- GCC_except_table275
- GCC_except_table278
- GCC_except_table281
- GCC_except_table44
- GCC_except_table46
- GCC_except_table96
- GCC_except_table99
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-578.60.14.0.2~23, %s file: %s, line: %d\n\n"
+ "BKBioConvenienceEnabled"
+ "BKDeviceConvenience.m"
+ "BKDeviceConvenience::bioLockoutState:forUser: %p, %u (_cid:%lu)\n"
+ "BKDeviceConvenience::bioLockoutState:forUser: -> %d, state:%ld, disabledInAKS:%d, error:%@\n"
+ "BKDeviceConvenience::createMatchOperation\n"
+ "BKDeviceConvenience::createMatchOperation -> %@, error:%@\n"
+ "BKDeviceConvenience::deviceAvailableWithFailure -> %d, failure:%d\n"
+ "BKDeviceConvenience::deviceAvailableWithFailure: %p\n"
+ "BKDeviceConvenience::extendedBioLockoutState:forUser: %p, %u (_cid:%lu)\n"
+ "BKDeviceConvenience::extendedBioLockoutState:forUser: -> %d, state:%ld, disabledInAKS:%d, error:%@\n"
+ "BKDeviceConvenience::identities (_cid:%lu)\n"
+ "BKDeviceConvenience::identities -> %lu, disabledInAKS:%d, error:%@\n"
+ "BKDeviceConvenience::identitiesForUser: %u (_cid:%lu)\n"
+ "BKDeviceConvenience::identitiesForUser: -> %lu, disabledInAKS:%d, error:%@\n"
+ "BKDeviceConvenience::prewarm (_cid:%lu)\n"
+ "BKDeviceConvenience::prewarm -> %d, error:%@\n"
+ "BKMatchConvenienceOperation::enableAutoRetry -> %d(err:0x%x), error:%@\n"
+ "BKMatchConvenienceOperation::enableAutoRetry: %d (_cid:%lu)\n"
+ "BKOptionMatchConvenienceCameraType"
+ "BKOptionMatchConvenienceIdentityUpdateOnly"
+ "ExclaveCapability"
+ "[BKDeviceConvenience deviceAvailableWithFailure:((void*)0)]"
+ "com.apple.BKDeviceConvenience.dispatch"
+ "com.apple.ClarityBoard"
+ "com.apple.Preferences"
+ "com.apple.bioconvenienced"
+ "com.apple.keystore.conveniencebio.created"
+ "com.apple.keystore.conveniencebio.unavailable"
+ "com.apple.managedconfiguration.profiled"
+ "com.apple.private.biometrickit.allow-bioconvenience"
+ "com.apple.springboard"
+ "getAKSConfigurationFlags: aks_get_configuration -> 0x%x\n"
+ "isBioConvenienceClientAllowed: %{public}@ -> %u (hasEntitlement: %u, allowListed: %u)\n"
+ "isBioConveniencePlatform: %u\n"
+ "status == 0"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-578.60.5.0.4~21, %s file: %s, line: %d\n\n"
```
