## MessageProtection

> `/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection`

```diff

-398.0.0.0.0
-  __TEXT.__text: 0x77738
+398.40.2.0.0
+  __TEXT.__text: 0x77b1c
   __TEXT.__objc_methlist: 0x2374
-  __TEXT.__cstring: 0x3197
+  __TEXT.__cstring: 0x31f7
   __TEXT.__const: 0x57c4
-  __TEXT.__oslogstring: 0x25e1
+  __TEXT.__oslogstring: 0x2673
   __TEXT.__gcc_except_tab: 0x414
   __TEXT.__ustring: 0x21c
   __TEXT.__constg_swiftt: 0x1398

   __DATA_CONST.__objc_selrefs: 0xf70
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x128
-  __DATA_CONST.__got: 0x618
+  __DATA_CONST.__got: 0x620
   __AUTH_CONST.__const: 0x26e8
   __AUTH_CONST.__cfstring: 0x18a0
   __AUTH_CONST.__objc_const: 0x6200
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__auth_got: 0x11a8
+  __AUTH_CONST.__auth_got: 0x11b0
   __AUTH.__objc_data: 0x3f0
   __AUTH.__data: 0x220
   __DATA.__objc_ivar: 0x178

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 2586
-  Symbols:   7183
-  CStrings:  520
+  Symbols:   7185
+  CStrings:  523
 
Symbols:
+ _$s10Foundation4DataV15_RepresentationOys5UInt8VSicis
+ _$s17MessageProtection29TetraIncomingSymmetricRatchetV04openA0_12messageIndex0H12KeyIndicator07discardaJ0020onChainWithReceivingJ0AA0c5InnerA0V10Foundation4DataV_s6UInt32VAMSb9CryptoKit4P256O0J9AgreementO06PublicJ0VSgtKF
+ _$ss6UInt64Vs23CustomStringConvertiblesWP
+ _swift_bridgeObjectRelease_n
- _$s10Foundation13__DataStorageC27ensureUniqueBufferReference9growingTo5clearySi_SbtF
- _$s17MessageProtection29TetraIncomingSymmetricRatchetV04openA0_12messageIndex0H12KeyIndicator07discardaJ0AA0c5InnerA0V10Foundation4DataV_s6UInt32VALSbtKF
Functions:
~ _$s17MessageProtection5I2OSP5value15outputByteCount10Foundation4DataVSi_SitF : 1168 -> 372
~ _$s17MessageProtection17TetraRatchetStateV04openA0_10sessionDST03didD0AA0c5InnerA0Vx_10Foundation4DataVSbXESbztKAA0c5OuterA0RzlFAA0c2NodmA0V_Tg5Tm : 1812 -> 2052
~ _$s17MessageProtection17TetraRatchetStateV13ratchetedOpen7message10sessionDST03didD0AA0c5InnerA0Vx_10Foundation4DataVSbXESbztKAA0c5OuterA0RzlFAA0c2NodoA0V_Tg5Tm : 8568 -> 8916
~ _$s17MessageProtection29TetraIncomingSymmetricRatchetV04openA0_12messageIndex0H12KeyIndicator07discardaJ0AA0c5InnerA0V10Foundation4DataV_s6UInt32VALSbtKF -> _$s17MessageProtection29TetraIncomingSymmetricRatchetV04openA0_12messageIndex0H12KeyIndicator07discardaJ0020onChainWithReceivingJ0AA0c5InnerA0V10Foundation4DataV_s6UInt32VAMSb9CryptoKit4P256O0J9AgreementO06PublicJ0VSgtKF : 1104 -> 2308
CStrings:
+ " indexes behind current location (previously derived key)"
+ "Mismatch in ratchet state on %s at index %llu for incoming index %u, attempting to decrypt with message key with indicator: %s instead of %s."
+ "Tetra ratchet on %s at index %llu opening incoming index %u, %s, with discardMessageKey: %{bool}d."
+ "Tetra ratchet on %s failed to provide the message key for incoming index %u at current index %llu: %s."
+ "unidentified chain"
- "Mismatch in ratchet state, attempting to decrypt with message key with indicator: %s instead of %s."
- "Tetra ratchet with current index %llu and incoming %u for delta of: %llu, and overflow %{bool}d "
```
