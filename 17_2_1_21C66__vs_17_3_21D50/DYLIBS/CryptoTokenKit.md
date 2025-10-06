## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-685.60.2.0.0
-  __TEXT.__text: 0x42070
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x3414
+685.80.2.0.0
+  __TEXT.__text: 0x42ac4
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x358c
   __TEXT.__gcc_except_tab: 0x108c
-  __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x27c0
-  __TEXT.__oslogstring: 0x2dc9
+  __TEXT.__const: 0x610
+  __TEXT.__cstring: 0x2971
+  __TEXT.__oslogstring: 0x2e43
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__unwind_info: 0x13b4
-  __TEXT.__objc_classname: 0xa99
-  __TEXT.__objc_methname: 0x75f7
-  __TEXT.__objc_methtype: 0x1c03
-  __TEXT.__objc_stubs: 0x5a00
+  __TEXT.__unwind_info: 0x13e8
+  __TEXT.__objc_classname: 0xaad
+  __TEXT.__objc_methname: 0x7a4c
+  __TEXT.__objc_methtype: 0x1c23
+  __TEXT.__objc_stubs: 0x5cc0
   __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x1360
-  __DATA_CONST.__objc_classlist: 0x290
+  __DATA_CONST.__const: 0x1348
+  __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x61b0
-  __DATA_CONST.__objc_selrefs: 0x1bf0
+  __DATA_CONST.__objc_const: 0x63c8
+  __DATA_CONST.__objc_selrefs: 0x1ce8
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x2080
-  __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__cfstring: 0x2200
+  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__auth_got: 0x578
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0xa0
-  __DATA.__objc_classrefs: 0x348
-  __DATA.__objc_superrefs: 0x238
-  __DATA.__objc_ivar: 0x4dc
+  __DATA.__objc_classrefs: 0x350
+  __DATA.__objc_superrefs: 0x240
+  __DATA.__objc_ivar: 0x500
   __DATA.__data: 0xe10
   __DATA.__bss: 0x110
-  __DATA_DIRTY.__const: 0x720
+  __DATA_DIRTY.__const: 0x5c0
   __DATA_DIRTY.__objc_const: 0x2010
   __DATA_DIRTY.__objc_data: 0x19a0
   __DATA_DIRTY.__bss: 0x2a8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5DC51B35-DEF5-385A-AA9C-AD7CE0F730E4
-  Functions: 1716
-  Symbols:   6155
-  CStrings:  2745
+  UUID: BE7C73BA-705B-395F-A6B5-3206CBAF8A3A
+  Functions: 1750
+  Symbols:   6260
+  CStrings:  2825
 
Symbols:
+ -[TKSlotParameters .cxx_destruct]
+ -[TKSlotParameters delegateWithControlMethod]
+ -[TKSlotParameters delegateWithEscapeMethod]
+ -[TKSlotParameters description]
+ -[TKSlotParameters displayMaxCharracters]
+ -[TKSlotParameters displayMaxLines]
+ -[TKSlotParameters firmwareVersion]
+ -[TKSlotParameters getDictionaryParameters]
+ -[TKSlotParameters initWithEntriesFromDictionary:]
+ -[TKSlotParameters initWithMaxBlockSize:]
+ -[TKSlotParameters interactionTimeout]
+ -[TKSlotParameters maxInputLength]
+ -[TKSlotParameters maxOutputLength]
+ -[TKSlotParameters maxPINLength]
+ -[TKSlotParameters minPINLength]
+ -[TKSlotParameters pinValidationCondition]
+ -[TKSlotParameters productID]
+ -[TKSlotParameters securePINChangeSupported]
+ -[TKSlotParameters securePINVerificationSupported]
+ -[TKSlotParameters setDelegateWithControlMethod:]
+ -[TKSlotParameters setDelegateWithEscapeMethod:]
+ -[TKSlotParameters setDisplayMaxCharracters:]
+ -[TKSlotParameters setDisplayMaxLines:]
+ -[TKSlotParameters setFirmwareVersion:]
+ -[TKSlotParameters setInteractionTimeout:]
+ -[TKSlotParameters setMaxInputLength:]
+ -[TKSlotParameters setMaxOutputLength:]
+ -[TKSlotParameters setMaxPINLength:]
+ -[TKSlotParameters setMinPINLength:]
+ -[TKSlotParameters setPinValidationCondition:]
+ -[TKSlotParameters setProductID:]
+ -[TKSlotParameters setSecurePINChangeSupported:]
+ -[TKSlotParameters setSecurePINVerificationSupported:]
+ -[TKSlotParameters setVendorID:]
+ -[TKSlotParameters vendorID]
+ -[TKSmartCardPINFormat PINBlockString]
+ -[TKSmartCardPINFormat PINFormatStringWithError:]
+ -[TKSmartCardPINFormat PINFormatStringWithError:].cold.1
+ -[TKSmartCardPINFormat PINLengthFormatWithError:]
+ -[TKSmartCardPINFormat PINLengthFormatWithError:].cold.1
+ -[TKSmartCardPINFormat PINMaxExtraDigit]
+ -[TKSmartCardSlot slotParameters]
+ -[TKSmartCardSlotEngine initWithSlotParameters:]
+ -[TKSmartCardSlotEngine slotParameters]
+ -[TKSmartCardUserInteractionForPINOperation localeID]
+ GCC_except_table100
+ GCC_except_table119
+ GCC_except_table140
+ GCC_except_table72
+ _OBJC_CLASS_$_TKSlotParameters
+ _OBJC_IVAR_$_TKSlotParameters._delegateWithControlMethod
+ _OBJC_IVAR_$_TKSlotParameters._delegateWithEscapeMethod
+ _OBJC_IVAR_$_TKSlotParameters._displayMaxCharracters
+ _OBJC_IVAR_$_TKSlotParameters._displayMaxLines
+ _OBJC_IVAR_$_TKSlotParameters._firmwareVersion
+ _OBJC_IVAR_$_TKSlotParameters._interactionTimeout
+ _OBJC_IVAR_$_TKSlotParameters._maxInputLength
+ _OBJC_IVAR_$_TKSlotParameters._maxOutputLength
+ _OBJC_IVAR_$_TKSlotParameters._maxPINLength
+ _OBJC_IVAR_$_TKSlotParameters._minPINLength
+ _OBJC_IVAR_$_TKSlotParameters._pinValidationCondition
+ _OBJC_IVAR_$_TKSlotParameters._productID
+ _OBJC_IVAR_$_TKSlotParameters._securePINChangeSupported
+ _OBJC_IVAR_$_TKSlotParameters._securePINVerificationSupported
+ _OBJC_IVAR_$_TKSlotParameters._vendorID
+ _OBJC_IVAR_$_TKSmartCardSlot._slotParameters
+ _OBJC_IVAR_$_TKSmartCardSlotEngine._slotParameters
+ _OBJC_METACLASS_$_TKSlotParameters
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _TKTransportSlotParameters
+ __OBJC_$_INSTANCE_METHODS_TKSlotParameters
+ __OBJC_$_INSTANCE_VARIABLES_TKSlotParameters
+ __OBJC_$_PROP_LIST_TKSlotParameters
+ __OBJC_CLASS_RO_$_TKSlotParameters
+ __OBJC_METACLASS_RO_$_TKSlotParameters
+ ___30-[TKSmartCardSlotEngine reset]_block_invoke.197
+ ___30-[TKSmartCardSlotEngine reset]_block_invoke.197.cold.1
+ ___32-[TKSmartCardSlot makeSmartCard]_block_invoke.120
+ ___34-[TKSmartCardSlotEngine terminate]_block_invoke.228
+ ___34-[TKSmartCardSlotEngine terminate]_block_invoke.228.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.214
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.217
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.219
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.224
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.216
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.216.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.218
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.218.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.223
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.223.cold.1
+ ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.240
+ ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.209
+ ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.210
+ ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.210.cold.1
+ ___37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.201
+ ___37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.201.cold.1
+ ___38-[TKSmartCardSlotEngine leaveSession:]_block_invoke.216
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.207
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.208
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.209
+ ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.275
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.381
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.381.cold.1
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.384
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.384.cold.1
+ ___46-[TKSmartCardSlotEngine scheduleIdlePowerDown]_block_invoke.205
+ ___49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.131
+ ___49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.131.cold.1
+ ___49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.134
+ ___49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.134.cold.1
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.214
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.214.cold.1
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.214.cold.2
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.215
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.215.cold.1
+ ___block_literal_global.119
+ ___block_literal_global.123
+ ___block_literal_global.203
+ ___block_literal_global.211
+ ___block_literal_global.212
+ ___block_literal_global.230
+ ___block_literal_global.235
+ ___block_literal_global.248
+ ___block_literal_global.251
+ ___block_literal_global.253
+ ___block_literal_global.380
+ ___block_literal_global.383
+ ___block_literal_global.386
+ ___block_literal_global.388
+ ___block_literal_global.416
+ ___block_literal_global.806
+ _class_copyPropertyList
+ _objc_msgSend$delegateWithControlMethod
+ _objc_msgSend$delegateWithEscapeMethod
+ _objc_msgSend$displayMaxCharracters
+ _objc_msgSend$displayMaxLines
+ _objc_msgSend$firmwareVersion
+ _objc_msgSend$getDictionaryParameters
+ _objc_msgSend$initWithEntriesFromDictionary:
+ _objc_msgSend$interactionTimeout
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$pinValidationCondition
+ _objc_msgSend$productID
+ _objc_msgSend$setDelegateWithControlMethod:
+ _objc_msgSend$setDelegateWithEscapeMethod:
+ _objc_msgSend$setMaxInputLength:
+ _objc_msgSend$setMaxOutputLength:
+ _objc_msgSend$setSecurePINChangeSupported:
+ _objc_msgSend$setSecurePINVerificationSupported:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$slotParameters
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$vendorID
+ _objc_msgSend$windowsLocaleCodeFromLocaleIdentifier:
+ _property_getName
- -[TKSmartCardSlot securePINChangeSupported]
- -[TKSmartCardSlot securePINVerificationSupported]
- -[TKSmartCardSlot setSecurePINChangeSupported:]
- -[TKSmartCardSlot setSecurePINVerificationSupported:]
- -[TKSmartCardSlotEngine init]
- -[TKSmartCardSlotEngine maxInputLength]
- -[TKSmartCardSlotEngine maxOutputLength]
- -[TKSmartCardSlotEngine securePINChangeSupported]
- -[TKSmartCardSlotEngine securePINVerificationSupported]
- -[TKSmartCardSlotEngine setMaxInputLength:]
- -[TKSmartCardSlotEngine setMaxOutputLength:]
- -[TKSmartCardSlotEngine setSecurePINChangeSupported:]
- -[TKSmartCardSlotEngine setSecurePINVerificationSupported:]
- GCC_except_table103
- GCC_except_table122
- GCC_except_table149
- GCC_except_table75
- _OBJC_IVAR_$_TKSmartCardSlot._maxInputLength
- _OBJC_IVAR_$_TKSmartCardSlot._maxOutputLength
- _OBJC_IVAR_$_TKSmartCardSlot._securePINChangeSupported
- _OBJC_IVAR_$_TKSmartCardSlot._securePINVerificationSupported
- _OBJC_IVAR_$_TKSmartCardSlotEngine._maxInputLength
- _OBJC_IVAR_$_TKSmartCardSlotEngine._maxOutputLength
- _OBJC_IVAR_$_TKSmartCardSlotEngine._securePINChangeSupported
- _OBJC_IVAR_$_TKSmartCardSlotEngine._securePINVerificationSupported
- _TKSmartCardSlotMaxInputLength
- _TKSmartCardSlotMaxOutputLength
- _TKSmartCardSlotSecurePINChangeSupportedKey
- _TKSmartCardSlotSecurePINVerificationSupportedKey
- ___30-[TKSmartCardSlotEngine reset]_block_invoke.193
- ___30-[TKSmartCardSlotEngine reset]_block_invoke.193.cold.1
- ___32-[TKSmartCardSlot makeSmartCard]_block_invoke.119
- ___34-[TKSmartCardSlotEngine terminate]_block_invoke.226
- ___34-[TKSmartCardSlotEngine terminate]_block_invoke.226.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.225
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.228
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.230
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.235
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.227
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.227.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.229
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.229.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.234
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.234.cold.1
- ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.251
- ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.202
- ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.202.cold.1
- ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.205
- ___37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.197
- ___37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.197.cold.1
- ___38-[TKSmartCardSlotEngine leaveSession:]_block_invoke.212
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.218
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.219
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.220
- ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.286
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.392
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.392.cold.1
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.395
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.395.cold.1
- ___46-[TKSmartCardSlotEngine scheduleIdlePowerDown]_block_invoke.201
- ___49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.127
- ___49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.127.cold.1
- ___49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.130
- ___49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.130.cold.1
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.210
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.210.cold.1
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.210.cold.2
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.211
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.211.cold.1
- ___block_literal_global.118
- ___block_literal_global.122
- ___block_literal_global.192
- ___block_literal_global.195
- ___block_literal_global.204
- ___block_literal_global.228
- ___block_literal_global.233
- ___block_literal_global.246
- ___block_literal_global.259
- ___block_literal_global.262
- ___block_literal_global.264
- ___block_literal_global.391
- ___block_literal_global.394
- ___block_literal_global.397
- ___block_literal_global.399
- ___block_literal_global.427
- ___block_literal_global.695
CStrings:
+ "\x01!\x13"
+ "    delegateWithControlMethod: %d\n"
+ "    delegateWithEscapeMethod: %d\n}\n"
+ "    displayMaxCharracters: %@\n"
+ "    displayMaxLines: %@ \n"
+ "    firmwareVersion: %@\n"
+ "    interactionTimeout: %f\n"
+ "    maxOutputLength: %ld\n"
+ "    maxPINLength: %@\n"
+ "    minPINLength: %@\n"
+ "    pinValidationCondition: %@ \n"
+ "    productID: %@\n"
+ "    securePINChangeSupported: %d\n"
+ "    securePINVerificationSupported: %d\n"
+ "    vendorID: %@\n"
+ "%{public}@: slot connected with parameters: %{public}@"
+ "6\x12"
+ "@\"TKSlotParameters\""
+ "A\x19\x12\x13"
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "C24@0:8^@16"
+ "PINBlockString"
+ "PINFormatStringWithError:"
+ "PINLengthFormatWithError:"
+ "PINMaxExtraDigit"
+ "T@\"NSNumber\",&,V_displayMaxCharracters"
+ "T@\"NSNumber\",&,V_displayMaxLines"
+ "T@\"NSNumber\",&,V_maxPINLength"
+ "T@\"NSNumber\",&,V_minPINLength"
+ "T@\"NSNumber\",&,V_pinValidationCondition"
+ "T@\"NSNumber\",&,V_productID"
+ "T@\"NSNumber\",&,V_vendorID"
+ "T@\"NSString\",&,V_firmwareVersion"
+ "T@\"TKSlotParameters\",R,C,V_slotParameters"
+ "TB,V_delegateWithControlMethod"
+ "TB,V_delegateWithEscapeMethod"
+ "TKSlotParameters"
+ "The 'PINBitOffset' is negative or can't fit"
+ "The 'PINLengthBitOffset' is negative or can't fit"
+ "_delegateWithControlMethod"
+ "_delegateWithEscapeMethod"
+ "_displayMaxCharracters"
+ "_displayMaxLines"
+ "_firmwareVersion"
+ "_pinValidationCondition"
+ "_productID"
+ "_slotParameters"
+ "_vendorID"
+ "delegateWithControlMethod"
+ "delegateWithEscapeMethod"
+ "displayMaxCharracters"
+ "displayMaxLines"
+ "engine:escape:"
+ "firmwareVersion"
+ "getDictionaryParameters"
+ "initWithEntriesFromDictionary:"
+ "initWithMaxBlockSize:"
+ "initWithSlotParameters:"
+ "localeID"
+ "localeIdentifier"
+ "params"
+ "pinValidationCondition"
+ "productID"
+ "setDelegateWithControlMethod:"
+ "setDelegateWithEscapeMethod:"
+ "setDisplayMaxCharracters:"
+ "setDisplayMaxLines:"
+ "setFirmwareVersion:"
+ "setPinValidationCondition:"
+ "setProductID:"
+ "setValue:forKey:"
+ "setVendorID:"
+ "slotParameters"
+ "valueForKey:"
+ "vendorID"
+ "windowsLocaleCodeFromLocaleIdentifier:"
+ "{\n    maxInputLength: %ld\n"
+ "\xf011"
- "\x01B!"
- "%{public}@: slot connected"
- "A\x191\x13"
- "Tq,R,N,V_maxInputLength"
- "Tq,R,N,V_maxOutputLength"
- "maxin"
- "maxout"
- "secpinchange"
- "secpinverify"
- "\xf0A1"

```
