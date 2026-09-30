## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1338.0.0.0.0
-  __TEXT.__text: 0x423f0
+1341.0.0.0.0
+  __TEXT.__text: 0x42384
   __TEXT.__auth_stubs: 0xd60
   __TEXT.__objc_stubs: 0x7be0
   __TEXT.__objc_methlist: 0x3590
-  __TEXT.__const: 0xf8
+  __TEXT.__const: 0x128
   __TEXT.__gcc_except_tab: 0x1054
   __TEXT.__cstring: 0x28ba
   __TEXT.__objc_methname: 0xc4d2
-  __TEXT.__oslogstring: 0x9ae7
+  __TEXT.__oslogstring: 0x9bb6
   __TEXT.__objc_classname: 0x6c3
   __TEXT.__objc_methtype: 0x3665
   __TEXT.__dlopen_cstrs: 0x56
Functions:
~ sub_1000108d4 : 368 -> 372
~ sub_100010b10 -> sub_100010b14 : 936 -> 940
~ sub_100023490 -> sub_100023498 : 1696 -> 1700
~ sub_100029a8c -> sub_100029a98 : 916 -> 788
~ sub_100029e20 -> sub_100029dac : 228 -> 232
~ sub_10003dd1c -> sub_10003dcac : 396 -> 400
CStrings:
+ "Error: Failed to fetch balance reminder for pass %{private}@ due to %@"
+ "Error: Watch fails to set balance reminder %@ for balance %{private}@ of pass %@"
+ "Notice: (PKPaymentBalance get) Request for balances for unique ID %@; returning %{private}@"
+ "Notice: (PKPaymentBalance set) Got updated balances %{private}@ for pass with unique ID %@. Processing subject to first unlock and paired sync."
+ "Notice: (PKPaymentBalanceReminder set) Got updated balance reminder %@ for balance %{private}@ and pass with unique ID %@. Processing subject to first unlock and paired sync."
+ "Notice: (account-pass-provisioning) companion no longer has pass for accountIdentifier %{private}@ will not reprovision"
+ "Notice: (account-pass-provisioning) companion still has pass for accountIdentifier %{private}@ will attempt reprovision"
+ "Notice: (account-pass-provisioning) handleDeviceUnlockedForPendingProvisioningRequestFromGizmo %{private}@ completion %@ %@"
+ "Notice: (account-pass-provisioning) handleDeviceUnlockedForPendingProvisioningRequestFromGizmo accountIdentifier %{private}@ makeDefault %@"
+ "Notice: (account-pass-provisioning) handleProvisioningErrorForAccountIdentifier %{private}@"
+ "Notice: (account-pass-provisioning) provisionCompletion for %{private}@ success %@"
+ "Notice: (account-pass-provisioning) provisionPassForAccountIdentifier %{private}@ makeDefault %@"
+ "Notice: (apple-balance-pass-provisioning) provisionPassForRemoteCredentialType %ld identifier: %{private}@ "
+ "Notice: Applied subcredentials %{private}@\n to pass with unique id %@\n applet %{private}@\n"
+ "Notice: Companion pass library submit verification code %{private}@ %{private}@ %@"
+ "Notice: Got balance reminder: %@ for balance %{private}@ and pass with unique ID %@; sending to %@"
+ "Notice: Got balances: %{private}@ for pass with unique ID %@; sending to %@"
+ "Notice: Handle push token: %{private}@ (current %{private}@)"
+ "Notice: Re-registering with push token %{private}@"
+ "Notice: Request to set balance reminder %@ for balance %{private}@ of pass %@"
- "Error: Failed to fetch balance reminder for pass %@ due to %@"
- "Error: Watch fails to set balance reminder %@ for balance %@ of pass %@"
- "Notice: (PKPaymentBalance get) Request for balances for unique ID %@; returning %@"
- "Notice: (PKPaymentBalance set) Got updated balances %@ for pass with unique ID %@. Processing subject to first unlock and paired sync."
- "Notice: (PKPaymentBalanceReminder set) Got updated balance reminder %@ for balance %@ and pass with unique ID %@. Processing subject to first unlock and paired sync."
- "Notice: (account-pass-provisioning) companion no longer has pass for accountIdentifier %@ will not reprovision"
- "Notice: (account-pass-provisioning) companion still has pass for accountIdentifier %@ will attempt reprovision"
- "Notice: (account-pass-provisioning) handleDeviceUnlockedForPendingProvisioningRequestFromGizmo %@ completion %@ %@"
- "Notice: (account-pass-provisioning) handleDeviceUnlockedForPendingProvisioningRequestFromGizmo accountIdentifier %@ makeDefault %@"
- "Notice: (account-pass-provisioning) handleProvisioningErrorForAccountIdentifier %@"
- "Notice: (account-pass-provisioning) provisionCompletion for %@ success %@"
- "Notice: (account-pass-provisioning) provisionPassForAccountIdentifier %@ makeDefault %@"
- "Notice: (apple-balance-pass-provisioning) provisionPassForRemoteCredentialType %ld identifier: %@ "
- "Notice: Applied subcredentials %@\n to pass with unique id %@\n applet %@\n"
- "Notice: Companion pass library submit verification code %@ %@ %@"
- "Notice: Got balance reminder: %@ for balance %@ and pass with unique ID %@; sending to %@"
- "Notice: Got balances: %@ for pass with unique ID %@; sending to %@"
- "Notice: Handle push token: %@ (current %@)"
- "Notice: Re-registering with push token %@"
- "Notice: Request to set balance reminder %@ for balance %@ of pass %@"
```
