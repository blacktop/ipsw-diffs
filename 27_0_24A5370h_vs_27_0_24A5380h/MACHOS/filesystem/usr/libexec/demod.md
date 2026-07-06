## demod

> `/usr/libexec/demod`

```diff

-  __TEXT.__text: 0xf3368
-  __TEXT.__auth_stubs: 0x20a0
-  __TEXT.__objc_stubs: 0x1b360
-  __TEXT.__objc_methlist: 0xd5ac
+  __TEXT.__text: 0xf43d4
+  __TEXT.__auth_stubs: 0x20b0
+  __TEXT.__objc_stubs: 0x1b480
+  __TEXT.__objc_methlist: 0xd944
   __TEXT.__const: 0x510
-  __TEXT.__cstring: 0x10b22
-  __TEXT.__objc_classname: 0x184a
-  __TEXT.__objc_methtype: 0x3d5b
-  __TEXT.__gcc_except_tab: 0x4680
-  __TEXT.__oslogstring: 0x1c58c
-  __TEXT.__objc_methname: 0x2037d
+  __TEXT.__cstring: 0x10bb2
+  __TEXT.__objc_classname: 0x186a
+  __TEXT.__objc_methtype: 0x3fdb
+  __TEXT.__gcc_except_tab: 0x46bc
+  __TEXT.__oslogstring: 0x1c93c
+  __TEXT.__objc_methname: 0x20de1
   __TEXT.__swift5_typeref: 0x112
   __TEXT.__swift5_capture: 0x94
   __TEXT.__constg_swiftt: 0x80

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__unwind_info: 0x39f0
+  __TEXT.__unwind_info: 0x3a28
   __TEXT.__eh_frame: 0x310
   __DATA_CONST.__const: 0x31c0
-  __DATA_CONST.__cfstring: 0xebe0
-  __DATA_CONST.__objc_classlist: 0x718
+  __DATA_CONST.__cfstring: 0xec40
+  __DATA_CONST.__objc_classlist: 0x720
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x158
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x418

   __DATA_CONST.__objc_arrayobj: 0x468
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA_CONST.__auth_got: 0x1060
-  __DATA_CONST.__got: 0xd90
+  __DATA_CONST.__auth_got: 0x1068
+  __DATA_CONST.__got: 0xf10
   __DATA_CONST.__auth_ptr: 0x180
-  __DATA.__objc_const: 0x193e0
-  __DATA.__objc_selrefs: 0x7e88
-  __DATA.__objc_ivar: 0xb28
-  __DATA.__objc_data: 0x47b0
-  __DATA.__data: 0x2930
+  __DATA.__objc_const: 0x19710
+  __DATA.__objc_selrefs: 0x80c0
+  __DATA.__objc_ivar: 0xb34
+  __DATA.__objc_data: 0x4800
+  __DATA.__data: 0x2990
   __DATA.__bss: 0x990
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6024
-  Symbols:   1047
-  CStrings:  12779
+  Functions: 6048
+  Symbols:   1048
+  CStrings:  12896
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _dispatch_group_wait
CStrings:
+ "%s - New content detected; forcing full install of all manifest content."
+ "%s - New submanifest content requires a manifest reinstall to prevent data loss, but manifestInfo is nil (manifest was never received or persisted).  Submanifest content may overwrite previously installed manifest content."
+ "%s is called with SN %@."
+ "%s was called."
+ "-[MSDHomeManager _checkAndRepairPrimaryPreferredHubState]"
+ "-[MSDHomeManager setPrimaryPreferredHub:]"
+ "Failed to remove home '%{public}@'. Error code: %ld, description: %{public}@"
+ "ForceInstall"
+ "HMHomeDelegatePrivate"
+ "Home is in good state with primary preferred resident."
+ "Home is in odd state.  Intended primary preferred hub is not what DCOTA server is expecting.  Setting now to use %@ from previously %@..."
+ "Home is in odd state.  Intended resident (%@) is not the same as current resident (%@)."
+ "IntendedPrimaryPreferredHub"
+ "MSDScreenFacesRefresh"
+ "No homes present yet; waiting up to %dmin for homeManagerDidUpdateHomes."
+ "No homes to remove."
+ "No primary preferred hub set by server.  Home is in good state."
+ "Removing %lu home(s)."
+ "Successfully removed home '%{public}@'."
+ "T@\"NSDictionary\",&,V_dataStoreCache"
+ "TB,N,V_forceInstall"
+ "Timed out after %dmin waiting for homes to populate."
+ "Timed out after %dsec waiting for all homes to be removed."
+ "_checkAndRepairPrimaryPreferredHubState"
+ "_dataStoreCache"
+ "_forceInstall"
+ "_manifestVersionStringForSignedManifest:"
+ "checkAndRepairPrimaryPreferredHubState:"
+ "dataStoreCache"
+ "forceInstall"
+ "home:didAddAccessoryNetworkProtectionGroup:"
+ "home:didAddMediaSystem:"
+ "home:didAddResidentDevice:"
+ "home:didFailAccessorySetupWithError:"
+ "home:didRemoveAccessoryNetworkProtectionGroup:"
+ "home:didRemoveMediaSystem:"
+ "home:didRemoveResidentDevice:"
+ "home:didUpdateAccessControlForUser:"
+ "home:didUpdateAccessoryInvitationsForUser:"
+ "home:didUpdateAccessoryNetworkProtectionGroup:"
+ "home:didUpdateActionSet:isExecuting:"
+ "home:didUpdateApplicationDataForActionSet:"
+ "home:didUpdateApplicationDataForRoom:"
+ "home:didUpdateApplicationDataForServiceGroup:"
+ "home:didUpdateAreBulletinNotificationsSupported:"
+ "home:didUpdateAudioAnalysisClassifierOptions:"
+ "home:didUpdateAudioGroupsController:"
+ "home:didUpdateAutomaticSoftwareUpdateEnabled:"
+ "home:didUpdateAutomaticThirdPartyAccessorySoftwareUpdateEnabled:"
+ "home:didUpdateClipCaptionLocales:"
+ "home:didUpdateClipCaptioningEnabled:"
+ "home:didUpdateClipCaptioningEnabledCameras:"
+ "home:didUpdateDismissedWalletKeyUWBUnlockOnboarding:"
+ "home:didUpdateEventLogDuration:"
+ "home:didUpdateEventLogEnabled:"
+ "home:didUpdateHasOnboardedForWalletKey:"
+ "home:didUpdateHomeActivityState:isActivityStateHoldActive:activityStateHoldEndDate:transitionalStateEndDate:"
+ "home:didUpdateHomeActivityStateSchedule:"
+ "home:didUpdateLastExecutionDateForActionSet:"
+ "home:didUpdateLocation:"
+ "home:didUpdateMediaPassword:"
+ "home:didUpdateMediaPeerToPeerEnabled:"
+ "home:didUpdateMinimumMediaUserPrivilege:"
+ "home:didUpdateOnboardAudioAnalysis:"
+ "home:didUpdatePersonManagerSettings:"
+ "home:didUpdateReprovisionStateForAccessory:"
+ "home:didUpdateSiriPhraseOptions:"
+ "home:didUpdateStateForOutgoingInvitations:"
+ "home:didUpdateSupportsResidentActionSetStateEvaluation:"
+ "home:didUpdateTimeZone:"
+ "homeDidAddWalletKey:"
+ "homeDidEnableLocationServices:"
+ "homeDidEnableMultiUser:"
+ "homeDidOnboardLocationServices:"
+ "homeDidRemoveWalletKey:"
+ "homeDidSetEnableDoorbellChime:"
+ "homeDidSetHasAnyUserAcknowledgedCameraRecordingOnboarding:"
+ "homeDidSetHasOnboardedForAccessCode:"
+ "homeDidUpdateApplicationData:"
+ "homeDidUpdateAssistantIdentifiers:"
+ "homeDidUpdateAutoSelectedPreferredResident:"
+ "homeDidUpdateHomeLocationStatus:"
+ "homeDidUpdateNetworkRouterSupport:"
+ "homeDidUpdateOnboardedEventLog:"
+ "homeDidUpdatePrimaryResidentNetworkInfo:"
+ "homeDidUpdateProtectionMode:"
+ "homeDidUpdateSoundCheck:"
+ "homeDidUpdateSupportsResidentSelection:"
+ "homeDidUpdateToROAR:"
+ "homeDidUpdateUserSelectedPreferredResident:"
+ "mailto:"
+ "needsInstallation"
+ "normalizedUserID:"
+ "removeAllHomes"
+ "removeHome:completionHandler:"
+ "setDataStoreCache:"
+ "setForceInstall:"
+ "v28@0:8@\"HMHome\"16B24"
+ "v32@0:8@\"HMHome\"16@\"CLLocation\"24"
+ "v32@0:8@\"HMHome\"16@\"HMAccessoryNetworkProtectionGroup\"24"
+ "v32@0:8@\"HMHome\"16@\"HMHomeActivityStateSchedule\"24"
+ "v32@0:8@\"HMHome\"16@\"HMHomePersonManagerSettings\"24"
+ "v32@0:8@\"HMHome\"16@\"HMMediaGroupsController\"24"
+ "v32@0:8@\"HMHome\"16@\"HMMediaSystem\"24"
+ "v32@0:8@\"HMHome\"16@\"HMResidentDevice\"24"
+ "v32@0:8@\"HMHome\"16@\"NSArray\"24"
+ "v32@0:8@\"HMHome\"16@\"NSError\"24"
+ "v32@0:8@\"HMHome\"16@\"NSSet\"24"
+ "v32@0:8@\"HMHome\"16@\"NSString\"24"
+ "v32@0:8@\"HMHome\"16@\"NSTimeZone\"24"
+ "v32@0:8@\"HMHome\"16q24"
+ "v32@0:8@16q24"
+ "v36@0:8@\"HMHome\"16@\"HMActionSet\"24B32"
+ "v52@0:8@\"HMHome\"16Q24B32@\"NSDate\"36@\"NSDate\"44"
+ "v52@0:8@16Q24B32@36@44"
- "Device with serialNumber %{public}@ is already primary resident. Nothing to do."

```
