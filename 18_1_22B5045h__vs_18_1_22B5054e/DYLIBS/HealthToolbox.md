## HealthToolbox

> `/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox`

```diff

-5200.1.7.0.0
-  __TEXT.__text: 0x61a7c
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x6534
+5200.1.9.1.2
+  __TEXT.__text: 0x62d4c
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_methlist: 0x65ac
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x6f58
-  __TEXT.__oslogstring: 0x1d2d
-  __TEXT.__gcc_except_tab: 0x9f8
+  __TEXT.__cstring: 0x72a2
+  __TEXT.__oslogstring: 0x1dc7
+  __TEXT.__gcc_except_tab: 0xa84
   __TEXT.__dlopen_cstrs: 0x44
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x1a50
-  __TEXT.__objc_classname: 0x15d6
-  __TEXT.__objc_methname: 0x135e7
-  __TEXT.__objc_methtype: 0x2cf8
-  __TEXT.__objc_stubs: 0xed60
-  __DATA_CONST.__got: 0xc00
-  __DATA_CONST.__const: 0x1698
-  __DATA_CONST.__objc_classlist: 0x418
+  __TEXT.__unwind_info: 0x1a88
+  __TEXT.__objc_classname: 0x160b
+  __TEXT.__objc_methname: 0x13781
+  __TEXT.__objc_methtype: 0x2d0c
+  __TEXT.__objc_stubs: 0xef80
+  __DATA_CONST.__got: 0xc08
+  __DATA_CONST.__const: 0x1708
+  __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44a0
+  __DATA_CONST.__objc_selrefs: 0x4528
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x2a0
-  __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x50e0
-  __AUTH_CONST.__objc_const: 0xd530
+  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x5240
+  __AUTH_CONST.__objc_const: 0xd610
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_floatobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH.__objc_data: 0x2440
-  __DATA.__objc_ivar: 0x6f4
+  __AUTH.__objc_data: 0x2490
+  __DATA.__objc_ivar: 0x6fc
   __DATA.__data: 0x1020
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 2427
-  Symbols:   3080
-  CStrings:  4603
+  Functions: 2448
+  Symbols:   3104
+  CStrings:  4645
 
Symbols:
+ _OBJC_CLASS_$_HKSleepApneaUtilities
+ _HKDisplayTypeIdentifierToString
CStrings:
+ "\x03\x12\x16"
+ "_removePregnancyInformationFromMedicalID"
+ "upperBound"
+ "%!@(MISSING)"
+ "DELETE_ALL_PREGNANCY_INFORMATION_ALERT_DESCRIPTION"
+ "_removePregnancyInformationFromMedicalIDConfirmationSender:deleteBlock:"
+ "YES"
+ "sensitivity"
+ "DELETE_PREGNANCY_INFORMATION_ALERT_YES"
+ "yodel"
+ "tests"
+ "features"
+ "REMOVE_PREGNANCY_FROM_MEDICAL_ID_ALERT_DESCRIPTION"
+ "localizedTitleForBreathingDisturbances:"
+ "_medicalIDStore"
+ "setPregnancyStartDate:"
+ "leftEarClampingRangeUpperBound"
+ "pregnancyEstimatedDueDate"
+ "leftEarMasked"
+ "distantFuture"
+ "REMOVE_PREGNANCY_FROM_MEDICAL_ID_ALERT_TITLE"
+ "REMOVE_PREGNANCY_FROM_MEDICAL_ID_ALERT_PRIMARY_ACTION"
+ "Localizable-Yodel"
+ "WDAppleSleepingBreathingDisturbancesListDataProvider"
+ "Error updating Medical ID: %!{(MISSING)public}@"
+ "rightEarClampingRangeLowerBound"
+ "lowerBound"
+ "_fetchMedicalIDData"
+ "@\"HKMedicalIDStore\""
+ "DELETE_PREGNANCY_INFORMATION_ALERT_TITLE"
+ "side"
+ "B16@?0@\"HKAudiogramSensitivityTest\"8"
+ "rightEarMasked"
+ "rightEarClampingRangeUpperBound"
+ "masked"
+ "v20@?0Q8B16"
+ "leftEarClampingRangeLowerBound"
+ "View of kind UIAlertController already being presented. Not showing alert."
+ "clampingRange"
+ "setPregnancyEstimatedDueDate:"
+ "\n<!-- HealthKit Export Version: 14 -->\n<!ELEMENT HealthData (ExportDate,Me,(Record|Correlation|Workout|ActivitySummary|ClinicalRecord|Audiogram|VisionPrescription)*)>\n<!ATTLIST HealthData\n  locale CDATA #REQUIRED\n>\n<!ELEMENT ExportDate EMPTY>\n<!ATTLIST ExportDate\n  value CDATA #REQUIRED\n>\n<!ELEMENT Me EMPTY>\n<!ATTLIST Me\n  HKCharacteristicTypeIdentifierDateOfBirth                   CDATA #REQUIRED\n  HKCharacteristicTypeIdentifierBiologicalSex                 CDATA #REQUIRED\n  HKCharacteristicTypeIdentifierBloodType                     CDATA #REQUIRED\n  HKCharacteristicTypeIdentifierFitzpatrickSkinType           CDATA #REQUIRED\n  HKCharacteristicTypeIdentifierCardioFitnessMedicationsUse   CDATA #REQUIRED\n>\n<!ELEMENT Record ((MetadataEntry|HeartRateVariabilityMetadataList)*)>\n<!ATTLIST Record\n  type          CDATA #REQUIRED\n  unit          CDATA #IMPLIED\n  value         CDATA #IMPLIED\n  sourceName    CDATA #REQUIRED\n  sourceVersion CDATA #IMPLIED\n  device        CDATA #IMPLIED\n  creationDate  CDATA #IMPLIED\n  startDate     CDATA #REQUIRED\n  endDate       CDATA #REQUIRED\n>\n<!-- Note: Any Records that appear as children of a correlation also appear as top-level records in this document. -->\n<!ELEMENT Correlation ((MetadataEntry|Record)*)>\n<!ATTLIST Correlation\n  type          CDATA #REQUIRED\n  sourceName    CDATA #REQUIRED\n  sourceVersion CDATA #IMPLIED\n  device        CDATA #IMPLIED\n  creationDate  CDATA #IMPLIED\n  startDate     CDATA #REQUIRED\n  endDate       CDATA #REQUIRED\n>\n<!ELEMENT Workout ((MetadataEntry|WorkoutEvent|WorkoutRoute|WorkoutStatistics)*)>\n<!ATTLIST Workout\n  workoutActivityType   CDATA #REQUIRED\n  duration              CDATA #IMPLIED\n  durationUnit          CDATA #IMPLIED\n  totalDistance         CDATA #IMPLIED\n  totalDistanceUnit     CDATA #IMPLIED\n  totalEnergyBurned     CDATA #IMPLIED\n  totalEnergyBurnedUnit CDATA #IMPLIED\n  sourceName            CDATA #REQUIRED\n  sourceVersion         CDATA #IMPLIED\n  device                CDATA #IMPLIED\n  creationDate          CDATA #IMPLIED\n  startDate             CDATA #REQUIRED\n  endDate               CDATA #REQUIRED\n>\n<!ELEMENT WorkoutActivity ((MetadataEntry)*)>\n<!ATTLIST WorkoutActivity\n  uuid                 CDATA #REQUIRED\n  startDate            CDATA #REQUIRED\n  endDate              CDATA #IMPLIED\n  duration             CDATA #IMPLIED\n  durationUnit         CDATA #IMPLIED\n>\n<!ELEMENT WorkoutEvent ((MetadataEntry)*)>\n<!ATTLIST WorkoutEvent\n  type                 CDATA #REQUIRED\n  date                 CDATA #REQUIRED\n  duration             CDATA #IMPLIED\n  durationUnit         CDATA #IMPLIED\n>\n<!ELEMENT WorkoutStatistics EMPTY>\n<!ATTLIST WorkoutStatistics\n  type                 CDATA #REQUIRED\n  startDate            CDATA #REQUIRED\n  endDate              CDATA #REQUIRED\n  average              CDATA #IMPLIED\n  minimum              CDATA #IMPLIED\n  maximum              CDATA #IMPLIED\n  sum                  CDATA #IMPLIED\n  unit                 CDATA #IMPLIED\n>\n<!ELEMENT WorkoutRoute ((MetadataEntry|FileReference)*)>\n<!ATTLIST WorkoutRoute\n  sourceName    CDATA #REQUIRED\n  sourceVersion CDATA #IMPLIED\n  device        CDATA #IMPLIED\n  creationDate  CDATA #IMPLIED\n  startDate     CDATA #REQUIRED\n  endDate       CDATA #REQUIRED\n>\n<!ELEMENT FileReference EMPTY>\n<!ATTLIST FileReference\n  path CDATA #REQUIRED\n>\n<!ELEMENT ActivitySummary EMPTY>\n<!ATTLIST ActivitySummary\n  dateComponents           CDATA #IMPLIED\n  activeEnergyBurned       CDATA #IMPLIED\n  activeEnergyBurnedGoal   CDATA #IMPLIED\n  activeEnergyBurnedUnit   CDATA #IMPLIED\n  appleMoveTime            CDATA #IMPLIED\n  appleMoveTimeGoal        CDATA #IMPLIED\n  appleExerciseTime        CDATA #IMPLIED\n  appleExerciseTimeGoal    CDATA #IMPLIED\n  appleStandHours          CDATA #IMPLIED\n  appleStandHoursGoal      CDATA #IMPLIED\n>\n<!ELEMENT MetadataEntry EMPTY>\n<!ATTLIST MetadataEntry\n  key   CDATA #REQUIRED\n  value CDATA #REQUIRED\n>\n<!-- Note: Heart Rate Variability records captured by Apple Watch may include an associated list of instantaneous beats-per-minute readings. -->\n<!ELEMENT HeartRateVariabilityMetadataList (InstantaneousBeatsPerMinute*)>\n<!ELEMENT InstantaneousBeatsPerMinute EMPTY>\n<!ATTLIST InstantaneousBeatsPerMinute\n  bpm  CDATA #REQUIRED\n  time CDATA #REQUIRED\n>\n<!ELEMENT ClinicalRecord EMPTY>\n<!ATTLIST ClinicalRecord\n  type              CDATA #REQUIRED\n  identifier        CDATA #REQUIRED\n  sourceName        CDATA #REQUIRED\n  sourceURL         CDATA #REQUIRED\n  fhirVersion       CDATA #REQUIRED\n  receivedDate      CDATA #REQUIRED\n  resourceFilePath  CDATA #REQUIRED\n>\n<!ELEMENT Audiogram ((MetadataEntry|SensitivityPoint)*)>\n<!ATTLIST Audiogram\n  type          CDATA #REQUIRED\n  sourceName    CDATA #REQUIRED\n  sourceVersion CDATA #IMPLIED\n  device        CDATA #IMPLIED\n  creationDate  CDATA #IMPLIED\n  startDate     CDATA #REQUIRED\n  endDate       CDATA #REQUIRED\n>\n<!ELEMENT SensitivityPoint EMPTY>\n<!ATTLIST SensitivityPoint\n  frequencyValue   CDATA #REQUIRED\n  frequencyUnit    CDATA #REQUIRED\n  leftEarValue     CDATA #IMPLIED\n  leftEarUnit      CDATA #IMPLIED\n  leftEarMasked      CDATA #IMPLIED\n  leftEarClampingRangeLowerBound   CDATA #IMPLIED\n  leftEarClampingRangeUpperBound   CDATA #IMPLIED\n  rightEarValue    CDATA #IMPLIED\n  rightEarUnit     CDATA #IMPLIED\n  rightEarMasked      CDATA #IMPLIED\n  rightEarClampingRangeLowerBound  CDATA #IMPLIED\n  rightEarClampingRangeUpperBound  CDATA #IMPLIED\n>\n<!ELEMENT VisionPrescription ((RightEye|LeftEye|Attachment|MetadataEntry)*)>\n<!ATTLIST VisionPrescription\n  type             CDATA #REQUIRED\n  dateIssued       CDATA #REQUIRED\n  expirationDate   CDATA #IMPLIED\n  brand            CDATA #IMPLIED\n>\n<!ELEMENT RightEye EMPTY>\n<!ATTLIST RightEye\n  sphere           CDATA #IMPLIED\n  sphereUnit       CDATA #IMPLIED\n  cylinder         CDATA #IMPLIED\n  cylinderUnit     CDATA #IMPLIED\n  axis             CDATA #IMPLIED\n  axisUnit         CDATA #IMPLIED\n  add              CDATA #IMPLIED\n  addUnit          CDATA #IMPLIED\n  vertex           CDATA #IMPLIED\n  vertexUnit       CDATA #IMPLIED\n  prismAmount      CDATA #IMPLIED\n  prismAmountUnit  CDATA #IMPLIED\n  prismAngle       CDATA #IMPLIED\n  prismAngleUnit   CDATA #IMPLIED\n  farPD            CDATA #IMPLIED\n  farPDUnit        CDATA #IMPLIED\n  nearPD           CDATA #IMPLIED\n  nearPDUnit       CDATA #IMPLIED\n  baseCurve        CDATA #IMPLIED\n  baseCurveUnit    CDATA #IMPLIED\n  diameter         CDATA #IMPLIED\n  diameterUnit     CDATA #IMPLIED\n>\n<!ELEMENT LeftEye EMPTY>\n<!ATTLIST LeftEye\n  sphere           CDATA #IMPLIED\n  sphereUnit       CDATA #IMPLIED\n  cylinder         CDATA #IMPLIED\n  cylinderUnit     CDATA #IMPLIED\n  axis             CDATA #IMPLIED\n  axisUnit         CDATA #IMPLIED\n  add              CDATA #IMPLIED\n  addUnit          CDATA #IMPLIED\n  vertex           CDATA #IMPLIED\n  vertexUnit       CDATA #IMPLIED\n  prismAmount      CDATA #IMPLIED\n  prismAmountUnit  CDATA #IMPLIED\n  prismAngle       CDATA #IMPLIED\n  prismAngleUnit   CDATA #IMPLIED\n  farPD            CDATA #IMPLIED\n  farPDUnit        CDATA #IMPLIED\n  nearPD           CDATA #IMPLIED\n  nearPDUnit       CDATA #IMPLIED\n  baseCurve        CDATA #IMPLIED\n  baseCurveUnit    CDATA #IMPLIED\n  diameter         CDATA #IMPLIED\n  diameterUnit     CDATA #IMPLIED\n>\n<!ELEMENT Attachment EMPTY>\n<!ATTLIST Attachment\n  identifier       CDATA #IMPLIED\n>\n"
+ "REMOVE_PREGNANCY_FROM_MEDICAL_ID_ALERT_SECONDARY_ACTION"
+ "NO"
+ "Error fetching medicalIDData: %!{(MISSING)public}@"
+ "_deleteAllPregnancySamplesConfirmationSender:deleteBlock:"
+ "displayTypeIdentifierString"
- "\x03\x12\x14"
- "leftEarSensitivity"
- "rightEarSensitivity"
- "\n<!-- HealthKit Export Version: 14 -->\n<!ELEMENT HealthData (ExportDate,Me,(Record|Correlation|Workout|ActivitySummary|ClinicalRecord|Audiogram|VisionPrescription)*)>\n<!ATTLIST HealthData\n  locale CDATA #REQUIRED\n>\n<!ELEMENT ExportDate EMPTY>\n<!ATTLIST ExportDate\n  value CDATA #REQUIRED\n>\n<!ELEMENT Me EMPTY>\n<!ATTLIST Me\n  HKCharacteristicTypeIdentifierDateOfBirth                   CDATA #REQUIRED\n  HKCharacteristicTypeIdentifierBiologicalSex                 CDATA #REQUIRED\n  HKCharacteristicTypeIdentifierBloodType                     CDATA #REQUIRED\n  HKCharacteristicTypeIdentifierFitzpatrickSkinType           CDATA #REQUIRED\n  HKCharacteristicTypeIdentifierCardioFitnessMedicationsUse   CDATA #REQUIRED\n>\n<!ELEMENT Record ((MetadataEntry|HeartRateVariabilityMetadataList)*)>\n<!ATTLIST Record\n  type          CDATA #REQUIRED\n  unit          CDATA #IMPLIED\n  value         CDATA #IMPLIED\n  sourceName    CDATA #REQUIRED\n  sourceVersion CDATA #IMPLIED\n  device        CDATA #IMPLIED\n  creationDate  CDATA #IMPLIED\n  startDate     CDATA #REQUIRED\n  endDate       CDATA #REQUIRED\n>\n<!-- Note: Any Records that appear as children of a correlation also appear as top-level records in this document. -->\n<!ELEMENT Correlation ((MetadataEntry|Record)*)>\n<!ATTLIST Correlation\n  type          CDATA #REQUIRED\n  sourceName    CDATA #REQUIRED\n  sourceVersion CDATA #IMPLIED\n  device        CDATA #IMPLIED\n  creationDate  CDATA #IMPLIED\n  startDate     CDATA #REQUIRED\n  endDate       CDATA #REQUIRED\n>\n<!ELEMENT Workout ((MetadataEntry|WorkoutEvent|WorkoutRoute|WorkoutStatistics)*)>\n<!ATTLIST Workout\n  workoutActivityType   CDATA #REQUIRED\n  duration              CDATA #IMPLIED\n  durationUnit          CDATA #IMPLIED\n  totalDistance         CDATA #IMPLIED\n  totalDistanceUnit     CDATA #IMPLIED\n  totalEnergyBurned     CDATA #IMPLIED\n  totalEnergyBurnedUnit CDATA #IMPLIED\n  sourceName            CDATA #REQUIRED\n  sourceVersion         CDATA #IMPLIED\n  device                CDATA #IMPLIED\n  creationDate          CDATA #IMPLIED\n  startDate             CDATA #REQUIRED\n  endDate               CDATA #REQUIRED\n>\n<!ELEMENT WorkoutActivity ((MetadataEntry)*)>\n<!ATTLIST WorkoutActivity\n  uuid                 CDATA #REQUIRED\n  startDate            CDATA #REQUIRED\n  endDate              CDATA #IMPLIED\n  duration             CDATA #IMPLIED\n  durationUnit         CDATA #IMPLIED\n>\n<!ELEMENT WorkoutEvent ((MetadataEntry)*)>\n<!ATTLIST WorkoutEvent\n  type                 CDATA #REQUIRED\n  date                 CDATA #REQUIRED\n  duration             CDATA #IMPLIED\n  durationUnit         CDATA #IMPLIED\n>\n<!ELEMENT WorkoutStatistics EMPTY>\n<!ATTLIST WorkoutStatistics\n  type                 CDATA #REQUIRED\n  startDate            CDATA #REQUIRED\n  endDate              CDATA #REQUIRED\n  average              CDATA #IMPLIED\n  minimum              CDATA #IMPLIED\n  maximum              CDATA #IMPLIED\n  sum                  CDATA #IMPLIED\n  unit                 CDATA #IMPLIED\n>\n<!ELEMENT WorkoutRoute ((MetadataEntry|FileReference)*)>\n<!ATTLIST WorkoutRoute\n  sourceName    CDATA #REQUIRED\n  sourceVersion CDATA #IMPLIED\n  device        CDATA #IMPLIED\n  creationDate  CDATA #IMPLIED\n  startDate     CDATA #REQUIRED\n  endDate       CDATA #REQUIRED\n>\n<!ELEMENT FileReference EMPTY>\n<!ATTLIST FileReference\n  path CDATA #REQUIRED\n>\n<!ELEMENT ActivitySummary EMPTY>\n<!ATTLIST ActivitySummary\n  dateComponents           CDATA #IMPLIED\n  activeEnergyBurned       CDATA #IMPLIED\n  activeEnergyBurnedGoal   CDATA #IMPLIED\n  activeEnergyBurnedUnit   CDATA #IMPLIED\n  appleMoveTime            CDATA #IMPLIED\n  appleMoveTimeGoal        CDATA #IMPLIED\n  appleExerciseTime        CDATA #IMPLIED\n  appleExerciseTimeGoal    CDATA #IMPLIED\n  appleStandHours          CDATA #IMPLIED\n  appleStandHoursGoal      CDATA #IMPLIED\n>\n<!ELEMENT MetadataEntry EMPTY>\n<!ATTLIST MetadataEntry\n  key   CDATA #REQUIRED\n  value CDATA #REQUIRED\n>\n<!-- Note: Heart Rate Variability records captured by Apple Watch may include an associated list of instantaneous beats-per-minute readings. -->\n<!ELEMENT HeartRateVariabilityMetadataList (InstantaneousBeatsPerMinute*)>\n<!ELEMENT InstantaneousBeatsPerMinute EMPTY>\n<!ATTLIST InstantaneousBeatsPerMinute\n  bpm  CDATA #REQUIRED\n  time CDATA #REQUIRED\n>\n<!ELEMENT ClinicalRecord EMPTY>\n<!ATTLIST ClinicalRecord\n  type              CDATA #REQUIRED\n  identifier        CDATA #REQUIRED\n  sourceName        CDATA #REQUIRED\n  sourceURL         CDATA #REQUIRED\n  fhirVersion       CDATA #REQUIRED\n  receivedDate      CDATA #REQUIRED\n  resourceFilePath  CDATA #REQUIRED\n>\n<!ELEMENT Audiogram ((MetadataEntry|SensitivityPoint)*)>\n<!ATTLIST Audiogram\n  type          CDATA #REQUIRED\n  sourceName    CDATA #REQUIRED\n  sourceVersion CDATA #IMPLIED\n  device        CDATA #IMPLIED\n  creationDate  CDATA #IMPLIED\n  startDate     CDATA #REQUIRED\n  endDate       CDATA #REQUIRED\n>\n<!ELEMENT SensitivityPoint EMPTY>\n<!ATTLIST SensitivityPoint\n  frequencyValue   CDATA #REQUIRED\n  frequencyUnit    CDATA #REQUIRED\n  leftEarValue     CDATA #IMPLIED\n  leftEarUnit      CDATA #IMPLIED\n  rightEarValue    CDATA #IMPLIED\n  rightEarUnit     CDATA #IMPLIED\n>\n<!ELEMENT VisionPrescription ((RightEye|LeftEye|Attachment|MetadataEntry)*)>\n<!ATTLIST VisionPrescription\n  type             CDATA #REQUIRED\n  dateIssued       CDATA #REQUIRED\n  expirationDate   CDATA #IMPLIED\n  brand            CDATA #IMPLIED\n>\n<!ELEMENT RightEye EMPTY>\n<!ATTLIST RightEye\n  sphere           CDATA #IMPLIED\n  sphereUnit       CDATA #IMPLIED\n  cylinder         CDATA #IMPLIED\n  cylinderUnit     CDATA #IMPLIED\n  axis             CDATA #IMPLIED\n  axisUnit         CDATA #IMPLIED\n  add              CDATA #IMPLIED\n  addUnit          CDATA #IMPLIED\n  vertex           CDATA #IMPLIED\n  vertexUnit       CDATA #IMPLIED\n  prismAmount      CDATA #IMPLIED\n  prismAmountUnit  CDATA #IMPLIED\n  prismAngle       CDATA #IMPLIED\n  prismAngleUnit   CDATA #IMPLIED\n  farPD            CDATA #IMPLIED\n  farPDUnit        CDATA #IMPLIED\n  nearPD           CDATA #IMPLIED\n  nearPDUnit       CDATA #IMPLIED\n  baseCurve        CDATA #IMPLIED\n  baseCurveUnit    CDATA #IMPLIED\n  diameter         CDATA #IMPLIED\n  diameterUnit     CDATA #IMPLIED\n>\n<!ELEMENT LeftEye EMPTY>\n<!ATTLIST LeftEye\n  sphere           CDATA #IMPLIED\n  sphereUnit       CDATA #IMPLIED\n  cylinder         CDATA #IMPLIED\n  cylinderUnit     CDATA #IMPLIED\n  axis             CDATA #IMPLIED\n  axisUnit         CDATA #IMPLIED\n  add              CDATA #IMPLIED\n  addUnit          CDATA #IMPLIED\n  vertex           CDATA #IMPLIED\n  vertexUnit       CDATA #IMPLIED\n  prismAmount      CDATA #IMPLIED\n  prismAmountUnit  CDATA #IMPLIED\n  prismAngle       CDATA #IMPLIED\n  prismAngleUnit   CDATA #IMPLIED\n  farPD            CDATA #IMPLIED\n  farPDUnit        CDATA #IMPLIED\n  nearPD           CDATA #IMPLIED\n  nearPDUnit       CDATA #IMPLIED\n  baseCurve        CDATA #IMPLIED\n  baseCurveUnit    CDATA #IMPLIED\n  diameter         CDATA #IMPLIED\n  diameterUnit     CDATA #IMPLIED\n>\n<!ELEMENT Attachment EMPTY>\n<!ATTLIST Attachment\n  identifier       CDATA #IMPLIED\n>\n"

```
