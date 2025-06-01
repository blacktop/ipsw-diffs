## HeartRhythmUI

> `/System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x3aa8c
+4146.4.18.0.0
+  __TEXT.__text: 0x3a92c
   __TEXT.__auth_stubs: 0x860
   __TEXT.__objc_methlist: 0x46b8
   __TEXT.__const: 0x1e0
   __TEXT.__cstring: 0x37c2
-  __TEXT.__oslogstring: 0x1125
+  __TEXT.__oslogstring: 0x10b6
   __TEXT.__gcc_except_tab: 0x2f0
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__unwind_info: 0xce8
   __TEXT.__objc_classname: 0xa6a
-  __TEXT.__objc_methname: 0xc738
+  __TEXT.__objc_methname: 0xc746
   __TEXT.__objc_methtype: 0x152e
   __TEXT.__objc_stubs: 0x95c0
-  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x60

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5c18
   __DATA_CONST.__objc_selrefs: 0x2a40
+  __DATA_CONST.__objc_classrefs: 0x448
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__objc_const: 0x1548
   __AUTH_CONST.__cfstring: 0x2f20
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x440
   __AUTH.__objc_data: 0xb40
-  __DATA.__objc_classrefs: 0x448
-  __DATA.__objc_superrefs: 0x180
   __DATA.__objc_ivar: 0x514
   __DATA.__data: 0x548
   __DATA.__bss: 0x48

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9DC4E8D2-8B04-34BD-862A-92893AF5F1AB
+  UUID: C540316B-AC70-3C8A-BFA9-27C0641D6D5B
   Functions: 1584
-  Symbols:   5559
+  Symbols:   5558
   CStrings:  3017
 
Symbols:
+ ___103-[HROnboardingElectrocardiogramUpdateAvailabilityViewController continueAndCheckForUpdateAvailability:]_block_invoke.264
+ ___105-[HRElectrocardiogramWatchAppInstallability checkElectrocardiogramAppInstallStateWithContext:completion:]_block_invoke.271
+ ___105-[HRElectrocardiogramWatchAppInstallability checkElectrocardiogramAppInstallStateWithContext:completion:]_block_invoke.279
+ ___105-[HRElectrocardiogramWatchAppInstallability checkElectrocardiogramAppInstallStateWithContext:completion:]_block_invoke.281
+ ___83-[HRAtrialFibrillationOnboardingManager _wrapUpOnboardingWithNotificationsEnabled:]_block_invoke.263
+ ___88-[HROnboardingElectrocardiogramSetupCompleteViewController _setUpElectrocardiogramQuery]_block_invoke.296
+ ___88-[HROnboardingElectrocardiogramSetupCompleteViewController _setUpElectrocardiogramQuery]_block_invoke_2.297
+ ___88-[HROnboardingElectrocardiogramSetupCompleteViewController _setUpElectrocardiogramQuery]_block_invoke_2.297.cold.1
+ ___88-[HROnboardingElectrocardiogramTakeRecordingViewController _setUpElectrocardiogramQuery]_block_invoke.323
+ ___88-[HROnboardingElectrocardiogramTakeRecordingViewController _setUpElectrocardiogramQuery]_block_invoke_2.324
+ ___88-[HROnboardingElectrocardiogramTakeRecordingViewController _setUpElectrocardiogramQuery]_block_invoke_2.324.cold.1
+ ___97-[HROnboardingElectrocardiogramAvailabilityViewController stackedButtonView:didTapButtonAtIndex:]_block_invoke.302
+ ___block_literal_global.262
+ ___block_literal_global.292
+ ___block_literal_global.301
- _HKFeatureIdentifierElectrocardiogramRecordingV1
- ___103-[HROnboardingElectrocardiogramUpdateAvailabilityViewController continueAndCheckForUpdateAvailability:]_block_invoke.240
- ___105-[HRElectrocardiogramWatchAppInstallability checkElectrocardiogramAppInstallStateWithContext:completion:]_block_invoke.247
- ___105-[HRElectrocardiogramWatchAppInstallability checkElectrocardiogramAppInstallStateWithContext:completion:]_block_invoke.255
- ___105-[HRElectrocardiogramWatchAppInstallability checkElectrocardiogramAppInstallStateWithContext:completion:]_block_invoke.257
- ___83-[HRAtrialFibrillationOnboardingManager _wrapUpOnboardingWithNotificationsEnabled:]_block_invoke.239
- ___88-[HROnboardingElectrocardiogramSetupCompleteViewController _setUpElectrocardiogramQuery]_block_invoke.272
- ___88-[HROnboardingElectrocardiogramSetupCompleteViewController _setUpElectrocardiogramQuery]_block_invoke_2.273
- ___88-[HROnboardingElectrocardiogramSetupCompleteViewController _setUpElectrocardiogramQuery]_block_invoke_2.273.cold.1
- ___88-[HROnboardingElectrocardiogramTakeRecordingViewController _setUpElectrocardiogramQuery]_block_invoke.299
- ___88-[HROnboardingElectrocardiogramTakeRecordingViewController _setUpElectrocardiogramQuery]_block_invoke_2.300
- ___88-[HROnboardingElectrocardiogramTakeRecordingViewController _setUpElectrocardiogramQuery]_block_invoke_2.300.cold.1
- ___97-[HROnboardingElectrocardiogramAvailabilityViewController stackedButtonView:didTapButtonAtIndex:]_block_invoke.278
- ___block_literal_global.238
- ___block_literal_global.268
- ___block_literal_global.277
CStrings:
+ "T@\"NSString\",?,R,C"
- "[%{public}@ %{public}@] -> Could not establish eligibility for ECG1 countryCode: %{public}@, Error: %{public}@"

```
