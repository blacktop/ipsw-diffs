## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__common`

```diff

-3600.68.45.0.0
-  __TEXT.__text: 0x3708a8
-  __TEXT.__auth_stubs: 0x3800
-  __TEXT.__objc_stubs: 0x472e0
-  __TEXT.__objc_methlist: 0x235e8
+3600.68.61.11.1
+  __TEXT.__text: 0x371fcc
+  __TEXT.__auth_stubs: 0x3840
+  __TEXT.__objc_stubs: 0x47440
+  __TEXT.__objc_methlist: 0x23710
   __TEXT.__const: 0xed40
   __TEXT.__dlopen_cstrs: 0x99d
-  __TEXT.__gcc_except_tab: 0x3a70
-  __TEXT.__cstring: 0x52b52
-  __TEXT.__oslogstring: 0x45808
+  __TEXT.__gcc_except_tab: 0x3aac
+  __TEXT.__cstring: 0x52dfa
+  __TEXT.__oslogstring: 0x45d7e
   __TEXT.__objc_classname: 0x51d5
-  __TEXT.__objc_methname: 0x61874
-  __TEXT.__objc_methtype: 0xff0f
+  __TEXT.__objc_methname: 0x61bac
+  __TEXT.__objc_methtype: 0xff45
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0xa4e8
+  __TEXT.__unwind_info: 0xa520
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0x143e8
-  __DATA_CONST.__cfstring: 0x12320
+  __DATA_CONST.__cfstring: 0x123e0
   __DATA_CONST.__objc_classlist: 0xd40
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x728

   __DATA_CONST.__objc_superrefs: 0xb10
   __DATA_CONST.__objc_arraydata: 0x480
   __DATA_CONST.__objc_arrayobj: 0x198
-  __DATA_CONST.__objc_intobj: 0x8b8
+  __DATA_CONST.__objc_intobj: 0x8d0
   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x1c10
-  __DATA_CONST.__got: 0x3e80
+  __DATA_CONST.__auth_got: 0x1c30
+  __DATA_CONST.__got: 0x3e78
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x34b30
-  __DATA.__objc_selrefs: 0x15540
-  __DATA.__objc_ivar: 0x267c
+  __DATA.__objc_const: 0x34c58
+  __DATA.__objc_selrefs: 0x155e0
+  __DATA.__objc_ivar: 0x2694
   __DATA.__objc_data: 0x8480
   __DATA.__data: 0x5d60
   __DATA.__bss: 0xdd0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14601
-  Symbols:   3001
-  CStrings:  27824
+  Functions: 14626
+  Symbols:   3004
+  CStrings:  27881
 
Symbols:
+ _AFCanSyncIFPVoices
+ _NSStringFromAFSiriRestrictionReasons
+ _objc_sync_enter
+ _objc_sync_exit
- _SANPMediaTypeVideoValue
CStrings:
+ "%s #IFToolbox Reinitializing Intelligence Toolbox Readiness delegate for locale: %{public}@"
+ "%s #SiriAvailability Synchronously updating capabilities for language code %@"
+ "%s #SiriAvailability recomputing: current locale changed"
+ "%s #hal Skipping context donation for type %{public}@: serialized context is nil"
+ "%s #hal Skipping context donation: nil type from metadata %@"
+ "%s #unredactedMeCard -cachedUnredactedMeCard invoked (meCard present: %d)"
+ "%s Asset manager is nil."
+ "%s Cannot re-initialize Intelligence Flow assets delegate, languageCode: '%{public}@' is invalid for locale creation."
+ "%s Cannot re-initialize Intelligence Flow assets delegate, languageCode: '%{public}@' is nil."
+ "%s Could not get AFHearablesExperienceManager shared instance to wire internal delegate"
+ "%s Dictation Sampling: Stopping adding audio samples after adding %ld bytes since the permit monitor requested an abort (e.g. background task expiration)."
+ "%s Dictation originates from the Siri app; forcing context clear to start a fresh dictation session."
+ "%s Reinitializing Intelligence Flow assets delegate for locale: %{public}@"
+ "%s Reply after the announce finished reading; completing %lu already-read announce(s) (current %@) instead of re-reading"
+ "%s Siri restriction imposed (%@) — disabling assistant"
+ "%s Synching Voice Trigger data in %f seconds (vtFireTime %llu requestedFireTime %llu)"
+ "%s Voice Trigger sync timer already scheduled to fire no later than %f seconds from now; not rescheduling (vtFireTime %llu requestedFireTime %llu)"
+ "%s siriAvailability is nil in _clearContextAndStartAssistantSessionWithInvocationContext:; triggering synchronous capabilities update"
+ "%s siriAvailability is nil in resumeSessionWithOptions:completion:; triggering synchronous capabilities update"
+ "%s ‼️ Forcing shake to dismiss for confirmation reject during announce! Active confirmation contexts: %@"
+ "%s 🫨🔍 ADDaemon: Internal delegate already wired, skipping"
+ "-[ADAssetManager registerAssetProvidersForLanguage:]"
+ "-[ADAssistantDataManager cachedUnredactedMeCard]"
+ "-[ADCommandCenter _clearContextAndStartAssistantSessionWithInvocationContext:]"
+ "-[ADCommandCenter handleSiriAvailabilityDidChange:]_block_invoke"
+ "-[ADCommandCenter resumeSessionWithOptions:completion:]_block_invoke"
+ "-[ADHearablesExperienceManager _wireInternalDelegateToClientManager]"
+ "-[ADSiriCapabilitiesStore handleCurrentLocaleDidChange:]"
+ "-[ADSiriCapabilitiesStore performFullUpdate]"
+ "-[ADSiriCapabilitiesStore updateCapabilitiesSynchronouslyForLanguageCode:]"
+ "-[AFMutableDeviceContext setSerializedContextSnapshot:withMetadata:]"
+ "37"
+ "@\"SAPerson\"16@0:8"
+ "ADSiriCapabilitiesStoreAvailabilityDidChangeNotification"
+ "ADSiriCapabilitiesStoreNewAvailabilityKey"
+ "ADSiriCapabilitiesStoreOldAvailabilityKey"
+ "MobileAssistantDaemons-3600.68.61.11.1"
+ "T@\"<AFHearablesExperienceManagerInternalDelegate>\",&,N,V_internalDelegateAdapter"
+ "TQ,N,V_voiceTriggerSyncFireTime"
+ "Ti,N,V_expressivityPreset"
+ "Ti,N,V_pacePreset"
+ "_expressivityPreset"
+ "_getIsLLMSiriAvailable"
+ "_internalDelegateAdapter"
+ "_pacePreset"
+ "_preferredMediaUserInfoSnapshot"
+ "_preferredMediaUserInfoSnapshotLock"
+ "_publishPreferredMediaUserInfoSnapshot"
+ "_voiceTriggerSyncFireTime"
+ "_wireInternalDelegateToClientManager"
+ "cachedUnredactedMeCard"
+ "com.apple.WebKit.GPU"
+ "com.apple.campo"
+ "expressivity_preset"
+ "handleCurrentLocaleDidChange:"
+ "handleSiriAvailabilityDidChange:"
+ "hasExpressivityPreset"
+ "hasPacePreset"
+ "internalDelegateAdapter"
+ "pace_preset"
+ "restrictionReasons"
+ "setExpressivityPreset:"
+ "setHasExpressivityPreset:"
+ "setHasPacePreset:"
+ "setInternalDelegateAdapter:"
+ "setIsLLMSiriAvailable:"
+ "setPacePreset:"
+ "setVoiceTriggerSyncFireTime:"
+ "unredactedMeCard"
+ "updateCapabilitiesSynchronouslyForLanguageCode:"
+ "voiceTriggerSyncFireTime"
+ "{?=\"expressivityPreset\"b1\"gender\"b1\"pacePreset\"b1}"
- "%s #IFToolbox Reinitializing Intelligence Toolbox Readiness delegate for new locale: %{public}@"
- "%s Asset manager is deallocated."
- "%s Cannot re-initialize Intelligence Flow assets delegate, new languageCode: '%{public}@' is invalid for locale creation."
- "%s Cannot re-initialize Intelligence Flow assets delegate, new languageCode: '%{public}@' is nil."
- "%s Interrupted media is video. It should not be resumed."
- "%s Reinitializing Intelligence Flow assets delegate for new locale: %{public}@"
- "%s Synching Voice Trigger data in %f seconds"
- "-[ADAssetManager languageCodeWasChangedTo:]_block_invoke"
- "-[ADSiriCapabilitiesStore updateCapabilitiesStore]"
- "15"
- "MobileAssistantDaemons-3600.68.45"
- "SiriExpressiveVoicesEnabled"
- "SiriSetup"
- "linwood_voices_seed"
- "{?=\"gender\"b1}"
```
