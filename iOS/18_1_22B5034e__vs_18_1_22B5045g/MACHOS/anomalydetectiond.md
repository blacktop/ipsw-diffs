## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-120.0.5.0.0
-  __TEXT.__text: 0x31ba9c
+120.0.8.0.0
+  __TEXT.__text: 0x31ce38
   __TEXT.__auth_stubs: 0x16c0
-  __TEXT.__objc_stubs: 0x8a20
-  __TEXT.__objc_methlist: 0x7cfc
-  __TEXT.__const: 0x85bd
-  __TEXT.__gcc_except_tab: 0xf6d0
-  __TEXT.__cstring: 0x19364
-  __TEXT.__oslogstring: 0xe24d
+  __TEXT.__objc_stubs: 0x8a80
+  __TEXT.__objc_methlist: 0x7d1c
+  __TEXT.__const: 0x8b7d
+  __TEXT.__gcc_except_tab: 0xf6f8
+  __TEXT.__cstring: 0x1913b
+  __TEXT.__oslogstring: 0xe7b7
   __TEXT.__objc_classname: 0x104c
-  __TEXT.__objc_methtype: 0x5e99
-  __TEXT.__objc_methname: 0xb36b
+  __TEXT.__objc_methtype: 0x5f32
+  __TEXT.__objc_methname: 0xb3bb
   __TEXT.__ustring: 0x10bc
-  __TEXT.__unwind_info: 0xb690
+  __TEXT.__unwind_info: 0xb790
   __TEXT.__eh_frame: 0x590
   __DATA_CONST.__auth_got: 0xb78
-  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__got: 0x560
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x21e78
-  __DATA_CONST.__cfstring: 0x5d20
+  __DATA_CONST.__const: 0x220c8
+  __DATA_CONST.__cfstring: 0x5ce0
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA.__objc_const: 0x110b8
-  __DATA.__objc_selrefs: 0x2a90
+  __DATA.__objc_selrefs: 0x2aa8
   __DATA.__objc_ivar: 0x908
   __DATA.__objc_data: 0x2e40
   __DATA.__data: 0x1ff0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15075
-  Symbols:   524
-  CStrings:  8424
+  Functions: 15098
+  Symbols:   563
+  CStrings:  8431
 
Symbols:
+ __ZN23CLKappaDeescalatorSteps13kForceBaseKeyE
+ __ZN18CLKappaDeescalator23kDeescalatorForceGPSKeyE
+ __ZN33CLSafetyDeescalatorJointDetection13kForceBaseKeyE
+ __ZN34CLSafetyDeescalatorProjectilePhone13kForceBaseKeyE
+ __ZN33CLKappaDeescalatorAutocorrelation10kConfigKeyE
+ __ZN21CLKappaDeescalatorAOI13kForceBaseKeyE
+ __ZN23CLSafetyDeescalatorGolf22kConfigurationDefaultsE
+ __ZN27CLKappaDeescalatorMovingGps10kConfigKeyE
+ __ZN33CLSafetyDeescalatorJointDetection22kConfigurationDefaultsE
+ __ZN22CLKappaDeescalatorUsha22kConfigurationDefaultsE
+ __ZN27CLKappaDeescalatorStaticGps22kConfigurationDefaultsE
+ __ZN34CLSafetyDeescalatorProjectilePhone22kConfigurationDefaultsE
+ __ZN24CLKappaDeescalatorSkiing10kConfigKeyE
+ __ZN28CLKappaDeescalatorWaterProxy22kConfigurationDefaultsE
+ __ZN23CLKappaDeescalatorSteps10kConfigKeyE
+ __ZN21CLKappaDeescalatorMAP22kConfigurationDefaultsE
+ __ZN28CLKappaDeescalatorWaterProxy10kConfigKeyE
+ __ZN28CLKappaDeescalatorQuiescence22kConfigurationDefaultsE
+ __ZN33CLKappaDeescalatorAutocorrelation22kConfigurationDefaultsE
+ __ZN21CLKappaDeescalatorMAP13kForceBaseKeyE
+ __ZN24CLKappaDeescalatorSkiing13kForceBaseKeyE
+ __ZN23CLKappaDeescalatorSteps22kConfigurationDefaultsE
+ __ZN27CLKappaDeescalatorStaticGps10kConfigKeyE
+ __ZN27CLKappaDeescalatorMovingGps22kConfigurationDefaultsE
+ __ZN33CLKappaDeescalatorTriggerClusters13kForceBaseKeyE
+ __ZN34CLSafetyDeescalatorProjectilePhone10kConfigKeyE
+ __ZN21CLKappaDeescalatorMAP10kConfigKeyE
+ __ZN22CLKappaDeescalatorUsha13kForceBaseKeyE
+ __ZN28CLKappaDeescalatorQuiescence10kConfigKeyE
+ __ZN22CLKappaDeescalatorUsha10kConfigKeyE
+ __ZN24CLKappaDeescalatorSkiing22kConfigurationDefaultsE
+ __ZN33CLKappaDeescalatorAutocorrelation13kForceBaseKeyE
+ __ZN23CLSafetyDeescalatorGolf10kConfigKeyE
+ __ZN23CLSafetyDeescalatorGolf13kForceBaseKeyE
+ __ZN33CLSafetyDeescalatorJointDetection10kConfigKeyE
+ __ZN28CLKappaDeescalatorWaterProxy13kForceBaseKeyE
+ __ZN27CLKappaDeescalatorStaticGps13kForceBaseKeyE
+ __ZN18CLKappaDeescalator27kDeescalatorTurnOffTwoLevelE
+ __ZN27CLKappaDeescalatorMovingGps13kForceBaseKeyE
CStrings:
+ "[de-AOI] mode,%!u(MISSING),hardcoded,%!d(MISSING),OTA-general,%!d(MISSING),OTA-specific,%!d(MISSING)"
+ "[de-AC] missing config"
+ "[de-MAP] missing config"
+ "[de-USHA] missing config"
+ "[M][UC] config-1,%!f(MISSING),config-2,%!f(MISSING),config-3,%!f(MISSING),config-4,%!f(MISSING),config-5,%!f(MISSING),config-6,%!f(MISSING),config-7,%!f(MISSING),config-8,%!f(MISSING),config-9,%!f(MISSING)"
+ "[de-JD] final - no-decision: UNSURE"
+ "[de-WP] no road information available, confirmation required"
+ "[de-JD] verifying same event: no communication (UNSURE)"
+ "[de-JD] precondition failed: verify same event but not unsure"
+ "[de-JD] RS did not have a trigger: no blind spot"
+ "[de-WP] dem condition not met"
+ "MartyForceLowSenseDetected"
+ "[de-JD] RS had a trigger but no blind spot"
+ "[de-JD] has not received local JD output"
+ "[de-JD] final - de-escalate: SURE-NONE"
+ "i32@0:8r^{CSSafetyDefault=Cfff}16@24"
+ "[de-JD] verifying same event: SURE-REAL (%!f(MISSING) < %!f(MISSING))"
+ "[de-SkiLift] deescalated at boundary, crashTimestamp:%!l(MISSING)lu, numDeescalationSkiLift:%!d(MISSING), numTriggersWithRecentSkiLiftDetected:%!d(MISSING), numTriggersWithTrueBtHint:%!d(MISSING)"
+ "[de-USHA] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}f,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}u,config-4,%!{(MISSING)public}u,debug-1a,%!{(MISSING)public}d,debug-1b,%!{(MISSING)public}d"
+ "[de-JD] RS had a trigger that could have a blind spot: UNSURE"
+ "[de-WP] roads nearby"
+ "[de-JD] Precondition not met: different modes"
+ "[de-MGPS] missing config"
+ "[de-Steps] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}f,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}u,config-4,%!{(MISSING)public}u,debug-1a,%!{(MISSING)public}f,debug-1b,%!{(MISSING)public}u,debug-1c,%!{(MISSING)public}u,debug-1d,%!{(MISSING)public}u,debug-1e,%!{(MISSING)public}f,debug-1f,%!{(MISSING)public}llu,debug-1g,%!{(MISSING)public}u,debug-1h,%!{(MISSING)public}f,debug-1i,%!{(MISSING)public}u,debug-1j,%!{(MISSING)public}u"
+ "radarWithResult:triggerUUID:ttrManagedMsl:eventType:error:formattedDate:"
+ "[de-PP] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}f,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}f,config-4,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}f,debug-1b,%!{(MISSING)public}f,debug-1c,%!{(MISSING)public}f,debug-1d,%!{(MISSING)public}f,debug-2a,%!{(MISSING)public}d,debug-2b,%!{(MISSING)public}d"
+ "[de-JD] verifying same event: no remote real trigger (hold)"
+ "[de-Qui] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}f,config-2,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}f,debug-1b,%!{(MISSING)public}f,debug-1c,%!{(MISSING)public}f,debug-1d,%!{(MISSING)public}f,debug-1e,%!{(MISSING)public}d,debug-1f,%!{(MISSING)public}d"
+ "[de-JD] final - no-decision"
+ "[de-JD] got sample for other mode me=%!u(MISSING) other=%!u(MISSING): UNSURE"
+ "boolThreshold:forKey:"
+ "[de-WP] empty road list, not near road"
+ "[de-SkiLift] feedTrigger path %!u(MISSING) martyPath %!u(MISSING)"
+ "[de-GLF] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}d,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}llu,debug-1b,%!{(MISSING)public}lu,debug-1c,%!{(MISSING)public}lu,debug-1d,%!{(MISSING)public}llu"
+ "[de-WP] no roads nearby, deescalate"
+ "[de-TC] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,debug-1a,%!{(MISSING)public}u,debug-1b,%!{(MISSING)public}llu"
+ "[de-TLS] proxyForCar bitmap %!{(MISSING)public}d"
+ "[de-WP] water proxy disabled"
+ "[de-SkiLift] feedTrigger found ski lift trigger, count:%!d(MISSING)"
+ "[de-WP] missing config"
+ "[de-WP] road info determined, exiting"
+ "[de-TLS] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}d,config-2,%!{(MISSING)public}d,config-3,%!{(MISSING)public}d,config-4,%!{(MISSING)public}d,config-5,%!{(MISSING)public}d,config-6,%!{(MISSING)public}f,config-7,%!{(MISSING)public}f,config-8,%!{(MISSING)public}f,config-9,%!{(MISSING)public}f,config-10,%!{(MISSING)public}f,config-11,%!{(MISSING)public}d,config-12,%!{(MISSING)public}f,config-13,%!{(MISSING)public}d,config-14,%!{(MISSING)public}d,config-15,%!{(MISSING)public}d,config-16,%!{(MISSING)public}d,config-17,%!{(MISSING)public}d,config-18,%!{(MISSING)public}d,config-19,%!{(MISSING)public}d,config-20,%!{(MISSING)public}f,config-21,%!{(MISSING)public}d"
+ "[de-TLS] imu confidence (%!{(MISSING)public}f, %!{(MISSING)public}f) (%!{(MISSING)public}f, %!{(MISSING)public}f) (%!{(MISSING)public}f, %!{(MISSING)public}f) (%!{(MISSING)public}llu, %!{(MISSING)public}f)"
+ "[de-JD] verifying same event: no communication (hold, UNSURE)"
+ "[de-TLS] force high sensitivity"
+ "{CSMartyTap2RadarConfirmation_struct=i@}32@0:8^@16q24"
+ "B32@0:8r^{CSSafetyDefault=Cfff}16@24"
+ "[de-AOI] missing feature mode case"
+ "f32@0:8r^{CSSafetyDefault=Cfff}16@24"
+ "[de-SGPS] missing config"
+ "[de-JD]: lack of new local trigger does not change our mind"
+ "[de-WP] btHint is set"
+ "[de-TLS] got bt hint, probably in car"
+ "[de-WP] rejecting road info with error = %!l(MISSING)d"
+ "[de-JD] RS was outside 'same event region'"
+ "[de-WP] bt hint set, nothing to do"
+ "[de-AOI] feedTrigger path %!u(MISSING) martyPath %!u(MISSING)"
+ "[de-JD] evaluating at min hold duration"
+ "[de-TLS] roadClass UNKNOWN_ROAD. Ignoring per configuration."
+ "[de-Ski] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}u,config-2,%!{(MISSING)public}u,config-3,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}d,debug-1b,%!{(MISSING)public}d"
+ "[de-WP] roads nearby, done"
+ "de-USHA"
+ "[de-TLS] De-escalating due to road distance"
+ "[de-AC] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}d,debug-1a,%!{(MISSING)public}d,debug-1b,%!{(MISSING)public}d,debug-1c,%!{(MISSING)public}d"
+ "[de-TLS] missing config"
+ "[de-WP] no road information available, de-escalating"
+ "[de-JD] already latched to sure-real"
+ "[M][UC] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}d,C,%!{(MISSING)public}d,debug-1,%!{(MISSING)public}f,debug-2,%!{(MISSING)public}f,debug-3,%!{(MISSING)public}f,debug-4,%!{(MISSING)public}f,debug-5,%!{(MISSING)public}f,debug-6,%!{(MISSING)public}f,debug-7,%!{(MISSING)public}f,debug-8,%!{(MISSING)public}f,debug-9,%!{(MISSING)public}f,debug-10,%!{(MISSING)public}f,debug-11,%!{(MISSING)public}f,debug-12,%!{(MISSING)public}f,debug-13,%!{(MISSING)public}f,debug-14,%!{(MISSING)public}f,debug-15,%!{(MISSING)public}f,debug-16,%!{(MISSING)public}f,debug-17,%!{(MISSING)public}f,debug-18,%!{(MISSING)public}f,debug-19,%!{(MISSING)public}f,debug-20,%!{(MISSING)public}f,debug-21,%!{(MISSING)public}f"
+ "[de-Qui] missing config"
+ "[de-TLS] two-level escalation min/max cand %!{(MISSING)public}d proxy %!{(MISSING)public}d ls %!{(MISSING)public}d"
+ "Please tell us more about what you were doing around %!@(MISSING) ... \n\nNote: Two files containing sensor data have been automatically attached to the radar. You can go to the Attachments and delete each file, as well as the original sysdiagnose, if you do not wish for the information to be sent to the team."
+ "[M][CC] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}d,C,%!{(MISSING)public}d,debug-1,%!{(MISSING)public}f,debug-2,%!{(MISSING)public}f,debug-3,%!{(MISSING)public}f,debug-4,%!{(MISSING)public}f,debug-5,%!{(MISSING)public}f,debug-6,%!{(MISSING)public}f,debug-7,%!{(MISSING)public}f,debug-8,%!{(MISSING)public}f,debug-9,%!{(MISSING)public}f,debug-10,%!{(MISSING)public}f,debug-11,%!{(MISSING)public}f,debug-12,%!{(MISSING)public}f,debug-13,%!{(MISSING)public}f,debug-14,%!{(MISSING)public}f,debug-15,%!{(MISSING)public}f,debug-16,%!{(MISSING)public}f,debug-17,%!{(MISSING)public}f"
+ "[SC] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}llu,C,%!{(MISSING)public}d,D,%!{(MISSING)public}d,E,%!{(MISSING)public}d,F,%!{(MISSING)public}d,G,%!{(MISSING)public}d,config-1,%!{(MISSING)public}f,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}f,config-4,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}u,debug-1b,%!{(MISSING)public}u,debug-1c,%!{(MISSING)public}u,debug-2a,%!{(MISSING)public}u,debug-2b,%!{(MISSING)public}u,debug-2c,%!{(MISSING)public}u,debug-2d,%!{(MISSING)public}u,debug-2e,%!{(MISSING)public}u,debug-2f,%!{(MISSING)public}u,debug-2g,%!{(MISSING)public}u,debug-2h,%!{(MISSING)public}u,debug-2i,%!{(MISSING)public}u,debug-2j,%!{(MISSING)public}u,debug-2k,%!{(MISSING)public}u,debug-2l,%!{(MISSING)public}u,debug-2m,%!{(MISSING)public}u,debug-2n,%!{(MISSING)public}u,debug-2o,%!{(MISSING)public}u,debug-2p,%!{(MISSING)public}u,debug-2o,%!{(MISSING)public}u"
+ "[de-TLS] ignoreUnknownRoads %!{(MISSING)public}d roadClass %!{(MISSING)public}d distance to road %!{(MISSING)public}f under %!{(MISSING)public}f passed %!{(MISSING)public}d"
+ "[de-JD] verifying same event: SURE-NONE (%!f(MISSING) >= %!f(MISSING))"
+ "[de-JD] disabled"
+ "[de-TC] condition met - isTriggerCluster:%!d(MISSING), isClusterInBeginningOfDrive:%!d(MISSING), isBTHintDetected:%!d(MISSING), rightBoundaryTs:%!l(MISSING)lu"
+ "[de-AOI] isNearAOI"
+ "[de-SkiLift] deescalated, crashTimestamp:%!l(MISSING)lu, numDeescalationSkiLift:%!d(MISSING), numTriggersWithRecentSkiLiftDetected:%!d(MISSING), numTriggersWithTrueBtHint:%!d(MISSING)"
+ "[de-SkiLift] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,debug-1a,%!{(MISSING)public}u,debug-1b,%!{(MISSING)public}u"
+ "[de-WP] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}u,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}f,config-4,%!{(MISSING)public}u,config-5,%!{(MISSING)public}u,config-6,%!{(MISSING)public}d,config-7,%!{(MISSING)public}f"
+ "[de-JD] new remote sample does not change our SURE-NONE state"
+ "[de-TLS] two-level escalation at boundary cand %!{(MISSING)public}d proxy %!{(MISSING)public}d ls %!{(MISSING)public}d"
+ "[de-AOI] Checking if near AOI"
+ "[de-JD] verifying same event: no local real trigger (hold, UNSURE)"
+ "[de-SGPS] missing crashtimestamp"
+ "B56@0:8i16@20B28q32^@40@48"
+ "-[CSMartyTap2Radar radarWithResult:triggerUUID:ttrManagedMsl:eventType:error:formattedDate:]"
+ "[de-SGPS] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}u,config-2,%!{(MISSING)public}u,force-1,%!{(MISSING)public}u,force-2,%!{(MISSING)public}u,debug-1a,%!{(MISSING)public}u,debug-1b,%!{(MISSING)public}u,debug-1c,%!{(MISSING)public}u,debug-1c,%!{(MISSING)public}u"
+ "[de-SkiLift] feedTrigger found true btHint in trigger, count:%!d(MISSING)"
+ "[de-JD] 'same event region' is undefined: UNSURE"
+ "[M][SC] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}llu,C,%!{(MISSING)public}d,D,%!{(MISSING)public}d,E,%!{(MISSING)public}d,F,%!{(MISSING)public}d,G,%!{(MISSING)public}d,H,%!{(MISSING)public}d,config-1,%!{(MISSING)public}f,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}f,config-4,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}u,debug-1b,%!{(MISSING)public}u,debug-1c,%!{(MISSING)public}u,debug-2a,%!{(MISSING)public}u,debug-2b,%!{(MISSING)public}u,debug-2c,%!{(MISSING)public}u,debug-2d,%!{(MISSING)public}u,debug-2e,%!{(MISSING)public}u,debug-2f,%!{(MISSING)public}u,debug-2g,%!{(MISSING)public}u,debug-2h,%!{(MISSING)public}u,debug-2i,%!{(MISSING)public}u,debug-2j,%!{(MISSING)public}u,debug-2k,%!{(MISSING)public}u,debug-2l,%!{(MISSING)public}u,debug-2m,%!{(MISSING)public}u,debug-2n,%!{(MISSING)public}u,debug-2o,%!{(MISSING)public}u,debug-2p,%!{(MISSING)public}u,debug-2q,%!{(MISSING)public}u"
+ "[de-AOI] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,debug-1a,%!{(MISSING)public}u,debug-2a,%!{(MISSING)public}zu"
+ "[de-TLS] imu coef too old"
+ "[de-TLS] rejecting invalid reason %!d(MISSING)"
+ "[de-JD] Precondition not met: not unsure"
+ "[de-JD] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}u,config-1,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}llu,debug-1b,%!{(MISSING)public}llu,debug-1c,%!{(MISSING)public}llu,debug-1d,%!{(MISSING)public}u,debug-1e,%!{(MISSING)public}f"
+ "[de-JD] received local lastRealTriggerTimestamp: %!l(MISSING)lu"
+ "[GravityAC] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}d,C,%!{(MISSING)public}d,config-1,%!{(MISSING)public}d,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}d,config-4,%!{(MISSING)public}f,debug-1,%!{(MISSING)public}llu,debug-2,%!{(MISSING)public}llu,debug-3,%!{(MISSING)public}d,debug-4,%!{(MISSING)public}f,debug-5,%!{(MISSING)public}d"
+ "[de-Qui] buffer size mismatch"
+ "[de-TC] deescalated at boundary, crashTimestamp:%!l(MISSING)lu, deescalationBoundary:%!l(MISSING)lu"
+ "[SC] config, %!f(MISSING), %!f(MISSING), %!f(MISSING), %!f(MISSING)"
+ "[de-JD] final - no-decision: SURE-REAL"
+ "[de-TLS] two-level no info min/max cand %!{(MISSING)public}d proxy %!{(MISSING)public}d ls %!{(MISSING)public}d"
+ "[de-JD] verifying same event: no local real trigger (SURE-NONE)"
+ "[de-MAP] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}u,debug-1a,%!{(MISSING)public}u,debug-1b,%!{(MISSING)public}u,debug-1c,%!{(MISSING)public}llu,debug-1d,%!{(MISSING)public}llu"
+ "[de-GLF] missing config"
+ "[de-JD] verifying same event: no remote real trigger (SURE-NONE)"
+ "[de-USHA] buffer size mismatch"
+ "[de-JD] internal enum has been changed"
+ "[de-TLS] Road Distance de-escalation condition met"
+ "[de-AOI] Near AOI, deescalate"
+ "[de-AOI] Trigger with BTHint found, continue with escalation choice"
+ "[de-JD] missing config"
+ "de-GLF"
+ "[de-TLS] imu cond passed"
+ "[de-WP] no road info, ambiguous"
+ "[de-JD] verifying same event: (hold, UNSURE) (%!f(MISSING) >= %!f(MISSING))"
+ "[de-JD] verifying same event: no JD feature (hold, UNSURE)"
+ "[de-JD] verifying same event: no JD feature (SURE-NONE)"
+ "[de-TC] condition met but missing window boundary"
+ "[de-MGPS] summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}u,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}u,debug-1a,%!{(MISSING)public}u,debug-1b,%!{(MISSING)public}u"
+ "[de-WP] gps %!f(MISSING)/%!f(MISSING) flat %!d(MISSING)/%!d(MISSING) conf %!f(MISSING)/%!f(MISSING) %!d(MISSING)f"
+ "[de-JD] RS was inside 'same event region'"
+ "[de-TLS] two-level de-escalation at boundary cand %!{(MISSING)public}d proxy %!{(MISSING)public}d ls %!{(MISSING)public}d"
+ "intThreshold:forKey:"
+ "[de-AOI] Not near AOI on list, continue with escalation choice"
+ "[de-SGPS] two level is off - escalating"
+ "[de-JD] received remote sample: [remote=%!l(MISSING)lu local=%!l(MISSING)lu]"
+ "[de-Steps] missing config"
+ "[de-WP] rejecting DEM error = %!d(MISSING)"
+ "[de-AOI] AOI mitigation disabled, continue with escalation choice"
+ "floatThreshold:forKey:"
+ "[de-Ski] missing config"
+ "[de-WP] no roads nearby"
- "[SC] Moving Gps missing count threshold"
- "[JDD] verifying same event: no local real trigger (hold, UNSURE)"
- "[JDD] received remote sample: [remote=%!l(MISSING)lu local=%!l(MISSING)lu]"
- "AOI feedTrigger path %!u(MISSING) martyPath %!u(MISSING)"
- "[SC] skiing missing audio threshold"
- "[JDD] verifying same event: no remote real trigger (hold)"
- "[WP] empty road list, not near road"
- "[JDD] RS was outside 'same event region'"
- "[WP] rejecting DEM error = %!d(MISSING)"
- "[JDD] verifying same event: SURE-REAL (%!f(MISSING) < %!f(MISSING))"
- "[JDD] verifying same event: no remote real trigger (SURE-NONE)"
- "[JDD] verifying same event: no JD feature (SURE-NONE)"
- "[SC] config, %!f(MISSING), %!f(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!u(MISSING), %!f(MISSING), %!f(MISSING), %!f(MISSING), %!f(MISSING), %!f(MISSING), %!u(MISSING), %!u(MISSING), %!f(MISSING), %!u(MISSING), %!u(MISSING), %!f(MISSING), %!f(MISSING), %!u(MISSING), %!u(MISSING), %!f(MISSING), %!d(MISSING), %!d(MISSING), %!f(MISSING)"
- "[JDD] verifying same event: no communication (UNSURE)"
- "[JDD] disabled"
- "[JDD] missing enabled config"
- "force high sensitivity"
- "[WP] road info determined, exiting"
- "[WP] no roads nearby, deescalate"
- "[SC] Static GPS missing stationary count config"
- "[WP] config-1,%!{(MISSING)public}d,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}f,config-4,%!{(MISSING)public}d,config-5,%!{(MISSING)public}d,config-6,%!{(MISSING)public}d,config-7,%!{(MISSING)public}f"
- "[WP] water proxy disabled"
- "proxyForCar bitmap %!{(MISSING)public}d"
- "[JDD] config-1,%!u(MISSING),config-2,%!f(MISSING)"
- "[SC] Static GPS missing crashtimestamp"
- "[M][UC] config-1,%!f(MISSING),config-2,%!f(MISSING),config-3,%!f(MISSING),config-4,%!f(MISSING),config-5,%!f(MISSING),config-6,%!f(MISSING),config-7,%!f(MISSING)"
- "[TLS] config config-1,%!{(MISSING)public}d,config-2,%!{(MISSING)public}d,config-3,%!{(MISSING)public}d,config-4,%!{(MISSING)public}d,config-5,%!{(MISSING)public}d,config-6,%!{(MISSING)public}f,config-7,%!{(MISSING)public}f,config-8,%!{(MISSING)public}f,config-9,%!{(MISSING)public}f,config-10,%!{(MISSING)public}f,config-11,%!{(MISSING)public}d,config-12,%!{(MISSING)public}f,config-13,%!{(MISSING)public}d,config-14,%!{(MISSING)public}d,config-15,%!{(MISSING)public}d,config-16,%!{(MISSING)public}d,config-17,%!{(MISSING)public}d,config-18,%!{(MISSING)public}d,config-19,%!{(MISSING)public}d,config-20,%!{(MISSING)public}f,config-21,%!{(MISSING)public}d\n"
- "deleteCurrentList"
- "[WP] gps %!f(MISSING)/%!f(MISSING) flat %!d(MISSING)/%!d(MISSING) conf %!f(MISSING)/%!f(MISSING) %!d(MISSING)f"
- "[JDD] RS was inside 'same event region'"
- "[WP] no road info, ambiguous"
- "[WP] roads nearby, done"
- "[JDD] already latched to sure-real"
- "[JDD] final - no-decision"
- "ignoreUnknownRoads %!{(MISSING)public}d roadClass %!{(MISSING)public}d distance to road %!{(MISSING)public}f under %!{(MISSING)public}f passed %!{(MISSING)public}d"
- "[JDD] RS had a trigger that could have a blind spot: UNSURE"
- "[JDD] final - no-decision: SURE-REAL"
- "-[CSMartyTap2Radar radarWithResult:triggerUUID:ttrManagedMsl:eventType:error:]"
- "SkiLift feedTrigger found true btHint in trigger, count:%!d(MISSING)"
- "[SC] peak pressure missing in fUshaPeakPressureThreshold"
- "[JDD] RS had a trigger but no blind spot"
- "[JDD]: lack of new local trigger does not change our mind"
- "[M][SC] "
- "got bt hint, probably in car"
- "[de-GLF] config-1,%!f(MISSING)"
- "[JDD] Precondition not met: not unsure"
- "[SC] triggerClusters condition met but missing window boundary"
- "[WP] rejecting road info with error = %!l(MISSING)d"
- "ForceEscalateGPS"
- "[JDD] verifying same event: SURE-NONE (%!f(MISSING) >= %!f(MISSING))"
- "two-level de-escalation at boundary cand %!{(MISSING)public}d proxy %!{(MISSING)public}d ls %!{(MISSING)public}d"
- "[JDD] got sample for other mode me=%!u(MISSING) other=%!u(MISSING): UNSURE"
- "radarWithResult:triggerUUID:ttrManagedMsl:eventType:error:"
- "[SC] quiescence missing pulse threshold"
- "[WP] dem condition not met"
- "[SC] Checking if near kappaAOI"
- "[JDD] verifying same event: no communication (hold, UNSURE)"
- "[SC] SkiLift deescalated, crashTimestamp:%!l(MISSING)lu, numDeescalationSkiLift:%!d(MISSING), numTriggersWithRecentSkiLiftDetected:%!d(MISSING), numTriggersWithTrueBtHint:%!d(MISSING)"
- "[WP] bt hint set, nothing to do"
- "[SC] steps missing fStepsPerMinuteThreshold"
- "two-level escalation min/max cand %!{(MISSING)public}d proxy %!{(MISSING)public}d ls %!{(MISSING)public}d"
- "[SC] TriggerCluster deescalated at boundary, crashTimestamp:%!l(MISSING)lu, deescalationBoundary:%!l(MISSING)lu"
- "imu cond passed"
- "[SC] Trigger with BTHint found, continue with escalation choice"
- "SkiLift feedTrigger path %!u(MISSING) martyPath %!u(MISSING)"
- "[JDD] received local lastRealTriggerTimestamp: %!l(MISSING)lu"
- "[WP] no road information available, de-escalating"
- "[JDD] internal enum has been changed"
- "De-escalating due to road distance"
- "[JDD] precondition failed: verify same event but not unsure"
- "roadClass UNKNOWN_ROAD. Ignoring per configuration."
- "[SC] Near kappaAOI, deescalate"
- "[JDD] new remote sample does not change our SURE-NONE state"
- "[SC] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}llu,C,%!{(MISSING)public}d,D,%!{(MISSING)public}d,E,%!{(MISSING)public}d,F,%!{(MISSING)public}d,G,%!{(MISSING)public}d,H,%!{(MISSING)public}d,I,%!{(MISSING)public}d,J,%!{(MISSING)public}d,K,%!{(MISSING)public}d,L,%!{(MISSING)public}d,M,%!{(MISSING)public}d,config-1,%!{(MISSING)public}f,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}d,config-4,%!{(MISSING)public}d,config-5,%!{(MISSING)public}d,config-6,%!{(MISSING)public}f,config-7,%!{(MISSING)public}f,config-8,%!{(MISSING)public}f,config-9,%!{(MISSING)public}f,config-10,%!{(MISSING)public}d,config-11,%!{(MISSING)public}d,config-12,%!{(MISSING)public}f,config-13,%!{(MISSING)public}d,config-14,%!{(MISSING)public}d,config-15,%!{(MISSING)public}f,config-16,%!{(MISSING)public}f,config-17,%!{(MISSING)public}d,config-18,%!{(MISSING)public}d,config-19,%!{(MISSING)public}f,config-20,%!{(MISSING)public}d,config-21,%!{(MISSING)public}d,debug-1a,%!{(MISSING)public}d,debug-1b,%!{(MISSING)public}d,debug-1c,%!{(MISSING)public}d,debug-1d,%!{(MISSING)public}d,debug-1e,%!{(MISSING)public}d,debug-1f,%!{(MISSING)public}d,debug-1g,%!{(MISSING)public}d,debug-1h,%!{(MISSING)public}d,debug-1i,%!{(MISSING)public}d,debug-1j,%!{(MISSING)public}d,debug-1k,%!{(MISSING)public}d,debug-1l,%!{(MISSING)public}llu,debug-1m,%!{(MISSING)public}d,debug-1n,%!{(MISSING)public}d,debug-1o,%!{(MISSING)public}d,debug-1p,%!{(MISSING)public}d,debug-1q,%!{(MISSING)public}d,debug-2a,%!{(MISSING)public}d,debug-2b,%!{(MISSING)public}d,debug-2c,%!{(MISSING)public}d,debug-2d,%!{(MISSING)public}d,debug-3a,%!{(MISSING)public}d,debug-3b,%!{(MISSING)public}f,debug-3c,%!{(MISSING)public}f,debug-3d,%!{(MISSING)public}d,debug-4a,%!{(MISSING)public}d,debug-4b,%!{(MISSING)public}d,debug-4c,%!{(MISSING)public}f,debug-4d,%!{(MISSING)public}d,debug-4e,%!{(MISSING)public}llu,debug-5a,%!{(MISSING)public}d,debug-5b,%!{(MISSING)public}d,debug-6a,%!{(MISSING)public}f,debug-6b,%!{(MISSING)public}f,debug-6c,%!{(MISSING)public}f,debug-6d,%!{(MISSING)public}f,debug-7a,%!{(MISSING)public}d,debug-7b,%!{(MISSING)public}d,debug-7c,%!{(MISSING)public}d,debug-8a,%!{(MISSING)public}d,debug-8b,%!{(MISSING)public}d,debug-9a,%!{(MISSING)public}d,debug-9b,%!{(MISSING)public}d,debug-9c,%!{(MISSING)public}d,debug-10a,%!{(MISSING)public}d,debug-10b,%!{(MISSING)public}d,debug-10c,%!{(MISSING)public}d,debug-11a,%!{(MISSING)public}d,debug-12a,%!{(MISSING)public}d,debug-12b,%!{(MISSING)public}d,debug-12c,%!{(MISSING)public}llu,debug-12d,%!{(MISSING)public}llu,debug-13a,%!{(MISSING)public}llu,debug-13b,%!{(MISSING)public}llu,debug-13c,%!{(MISSING)public}llu,debug-13d,%!{(MISSING)public}u,debug-13e,%!{(MISSING)public}f,debug-13f,%!{(MISSING)public}d\n"
- "SkiLift feedTrigger found ski lift trigger, count:%!d(MISSING)"
- "[SC] KappaAOI mitigation disabled, continue with escalation choice"
- "[de-PP] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}d,config-1,%!{(MISSING)public}f,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}f,config-4,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}f,debug-1b,%!{(MISSING)public}f,debug-1c,%!{(MISSING)public}f,debug-1d,%!{(MISSING)public}f,debug-2a,%!{(MISSING)public}d,debug-2b,%!{(MISSING)public}d\n"
- "[M][SC] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}llu,C,%!{(MISSING)public}d,D,%!{(MISSING)public}d,E,%!{(MISSING)public}d,F,%!{(MISSING)public}d,G,%!{(MISSING)public}d,H,%!{(MISSING)public}d,config-1,%!{(MISSING)public}f,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}f,config-4,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}d,debug-1b,%!{(MISSING)public}d,debug-1c,%!{(MISSING)public}d,debug-2a,%!{(MISSING)public}d,debug-2b,%!{(MISSING)public}d,debug-2c,%!{(MISSING)public}d,debug-2d,%!{(MISSING)public}d,debug-2e,%!{(MISSING)public}d,debug-2f,%!{(MISSING)public}d,debug-2g,%!{(MISSING)public}d,debug-2h,%!{(MISSING)public}d,debug-2i,%!{(MISSING)public}d,debug-2j,%!{(MISSING)public}d,debug-2k,%!{(MISSING)public}d,debug-2l,%!{(MISSING)public}d,debug-2m,%!{(MISSING)public}d,debug-2n,%!{(MISSING)public}d,debug-2o,%!{(MISSING)public}d,debug-2p,%!{(MISSING)public}d\n"
- "[de-GLF] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}d,mode,%!{(MISSING)public}u,config-1,%!{(MISSING)public}f,debug-1a,%!{(MISSING)public}llu,debug-1b,%!{(MISSING)public}lu,debug-1c,%!{(MISSING)public}lu,debug-1d,%!{(MISSING)public}llu\n"
- "[JDD] verifying same event: (hold, UNSURE) (%!f(MISSING) >= %!f(MISSING))"
- "B48@0:8i16@20B28q32^@40"
- "[JDD] RS did not have a trigger: no blind spot"
- "[SC] triggerClusters condition met - isTriggerCluster:%!d(MISSING), isClusterInBeginningOfDrive:%!d(MISSING), isBTHintDetected:%!d(MISSING), rightBoundaryTs:%!l(MISSING)lu"
- "[JDD] Precondition not met: different modes"
- "[WP] no road information available, confirmation required"
- "de-Usha"
- "de-Golf"
- "[SC] number of usha CP epoch threshold missing in fNumUshaCPEpochThreshold"
- "i32@0:8^@16q24"
- "[SC] steps missing fStepsSecondOpportunityLookbackLength"
- "[JDD] final - de-escalate: SURE-NONE"
- "[SC] number of usha FP epoch threshold missing in fNumUshaFPEpochThreshold"
- "turning off two level- escalating"
- "[JDD] missing threshold"
- "[SC] isNearAOI"
- "[JDD] final - no-decision: UNSURE"
- "[SC] steps missing fStepsCadenceThreshold"
- "[JDD] has not received local JD output"
- "imu confidence (%!{(MISSING)public}f, %!{(MISSING)public}f) (%!{(MISSING)public}f, %!{(MISSING)public}f) (%!{(MISSING)public}f, %!{(MISSING)public}f) (%!{(MISSING)public}llu, %!{(MISSING)public}f)"
- "[GravityAC] summary,,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}d,C,%!{(MISSING)public}d,,debug-1,%!{(MISSING)public}llu,debug-2,%!{(MISSING)public}llu,debug-3,%!{(MISSING)public}d,debug-4,%!{(MISSING)public}f,debug-5,%!{(MISSING)public}d,config-1,%!{(MISSING)public}d,config-2,%!{(MISSING)public}f,config-3,%!{(MISSING)public}d,config-4,%!{(MISSING)public}f"
- "[WP] no roads nearby"
- "[MAP] config-1,%!d(MISSING)"
- "[SC] Static GPS missing low speed config"
- "[SC] rejecting invalid reason %!d(MISSING)"
- "[SC] skiing missing pressure change threshold"
- "[WP] roads nearby"
- "[SC] autocorrelation missing threshold"
- "[SC] Not near kappaAOI on list, continue with escalation choice"
- "two-level no info min/max cand %!{(MISSING)public}d proxy %!{(MISSING)public}d ls %!{(MISSING)public}d"
- "[JDD] evaluating at min hold duration"
- "[SC] quiescence missing spin threshold"
- "[SC] spin missing fUshaCumulativeRotationThreshold threshold"
- "[WP] btHint is set"
- "[M][CC] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}d,C,%!{(MISSING)public}f,D,%!{(MISSING)public}f,E,%!{(MISSING)public}f,F,%!{(MISSING)public}f,G,%!{(MISSING)public}f,H,%!{(MISSING)public}f,I,%!{(MISSING)public}f,J,%!{(MISSING)public}f,K,%!{(MISSING)public}f,L,%!{(MISSING)public}d,M,%!{(MISSING)public}f,N,%!{(MISSING)public}f,O,%!{(MISSING)public}f,P,%!{(MISSING)public}f,Q,%!{(MISSING)public}f,R,%!{(MISSING)public}f,S,%!{(MISSING)public}f,T,%!{(MISSING)public}f\n"
- "Please tell us more about what you were doing around the time of the pop-up ... \n\nNote: Two files containing sensor data have been automatically attached to the radar. You can go to the Attachments and delete each file, as well as the original sysdiagnose, if you do not wish for the information to be sent to the team."
- "[SC] SkiLift deescalated at boundary, crashTimestamp:%!l(MISSING)lu, numDeescalationSkiLift:%!d(MISSING), numTriggersWithRecentSkiLiftDetected:%!d(MISSING), numTriggersWithTrueBtHint:%!d(MISSING)"
- "two-level escalation at boundary cand %!{(MISSING)public}d proxy %!{(MISSING)public}d ls %!{(MISSING)public}d"
- "[JDD] verifying same event: no local real trigger (SURE-NONE)"
- "[SC] buffer size mismatch"
- "Road Distance de-escalation condition met"
- "imu coef too old"
- "[de-PP] config-1,%!f(MISSING),config-2,%!f(MISSING),config-3,%!f(MISSING),config-4,%!f(MISSING)"
- "[M][UC] AlgBlock summary,A,%!{(MISSING)public}llu,B,%!{(MISSING)public}d,C,%!{(MISSING)public}f,D,%!{(MISSING)public}f,E,%!{(MISSING)public}f,F,%!{(MISSING)public}f,G,%!{(MISSING)public}f,H,%!{(MISSING)public}f,I,%!{(MISSING)public}f,J,%!{(MISSING)public}f,K,%!{(MISSING)public}f,L,%!{(MISSING)public}d,M,%!{(MISSING)public}f,N,%!{(MISSING)public}f,O,%!{(MISSING)public}f,P,%!{(MISSING)public}f,Q,%!{(MISSING)public}f,R,%!{(MISSING)public}f,S,%!{(MISSING)public}f,T,%!{(MISSING)public}f\n"
- "TurnOffTwoLevelSense"
- "[JDD] 'same event region' is undefined: UNSURE"
- "[SC] skiing missing baro threshold"
- "[SC] steps missing fStepsCountThreshold"
- "[JDD] verifying same event: no JD feature (hold, UNSURE)"

```
