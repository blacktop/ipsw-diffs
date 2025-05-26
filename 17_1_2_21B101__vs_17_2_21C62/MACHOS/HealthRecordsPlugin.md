## HealthRecordsPlugin

> `/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin`

```diff

-4146.1.11.3.0
-  __TEXT.__text: 0xae780
+4146.2.12.1.3
+  __TEXT.__text: 0xaff08
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_stubs: 0x12c20
-  __TEXT.__objc_methlist: 0x79f8
-  __TEXT.__objc_methname: 0x1c718
+  __TEXT.__objc_stubs: 0x12d60
+  __TEXT.__objc_methlist: 0x7a60
+  __TEXT.__objc_methname: 0x1c966
   __TEXT.__objc_classname: 0x1bfb
-  __TEXT.__objc_methtype: 0x3410
+  __TEXT.__objc_methtype: 0x3459
   __TEXT.__const: 0x14c
-  __TEXT.__gcc_except_tab: 0x1934
-  __TEXT.__cstring: 0xa087
-  __TEXT.__oslogstring: 0xe04a
-  __TEXT.__unwind_info: 0x279c
+  __TEXT.__gcc_except_tab: 0x1900
+  __TEXT.__cstring: 0xa055
+  __TEXT.__oslogstring: 0xe3c9
+  __TEXT.__unwind_info: 0x27c8
   __DATA_CONST.__auth_got: 0x6d0
-  __DATA_CONST.__got: 0x7f0
-  __DATA_CONST.__const: 0x36a8
-  __DATA_CONST.__cfstring: 0x77a0
+  __DATA_CONST.__got: 0x7f8
+  __DATA_CONST.__const: 0x3710
+  __DATA_CONST.__cfstring: 0x7780
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x158

   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0xe848
-  __DATA.__objc_selrefs: 0x5478
+  __DATA.__objc_selrefs: 0x54c8
   __DATA.__objc_classrefs: 0xb20
   __DATA.__objc_superrefs: 0x3a0
   __DATA.__objc_ivar: 0x704

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3433
-  Symbols:   741
-  CStrings:  5866
+  Functions: 3453
+  Symbols:   742
+  CStrings:  5885
 
Symbols:
+ _HKMedicalDownloadableAttachmentMetadataNeedsReIndexingKey
CStrings:
+ "%{public}@ %{public}@ did not insert original SCD record because %{public}@"
+ "%{public}@ Failed to recreate HKAttachmentReference for clinical records being re-inserted with error: %{private}@"
+ "%{public}@ Failed to recreate HKAttachmentReference for medical records being re-inserted with error: %{private}@"
+ "%{public}@ Failed to update MedicalDownloadableAttachments for medical records being re-inserted with error: %{private}@"
+ "%{public}@ failed to retrieve HDAttachments for existing clinicalRecord with UUID %{public}@. Error: %{private}@"
+ "%{public}@ failed to retrieve HDAttachments for existing medicalRecord with UUID %{public}@. Error: %{private}@"
+ "%{public}@ failed to update MedicalDownloadableAttachment for existing clinicalRecord with UUID %{public}@. Error: %{private}@"
+ "%{public}@ failed to update MedicalDownloadableAttachment for existing medicalRecord with UUID %{public}@. Error: %{private}@"
+ "%{public}@: _storeDataFromClinicalItem failed to retrieve SCD record extracted from existing original SCD record given its uniqueness checksum with error: %{public}@"
+ "B64@0:8@16@24@32@40@48^@56"
+ "B64@0:8@16@24@32^@40@48^@56"
+ "_attachmentIdentifierForMedicalRecordWithUUID:profile:error:"
+ "_attachmentMatchesDownloadableAttachment:hdAttachment:"
+ "_attachmentRefsForDownloadableAttachment:attachmentObjectIdentifier:profile:error:"
+ "_attachmentsAfterRelinkingFromClinicalRecord:toClinicalRecord:profile:error:"
+ "_attachmentsAfterRelinkingFromMedicalRecord:toMedicalRecord:profile:error:"
+ "_attachmentsForDownloadableAttachment:attachmentObjectIdentifier:profile:error:"
+ "_checkForObsoleteDownloadableAttachmentsForMedicalRecord:extractedDownloadableAttachments:medicalObjectIdentifier:clinicalObjectIdentifier:profile:error:"
+ "_clinicalRecordWithUUID:profile:error:"
+ "_deleteAttachmentsWithMedicalRecordIdentifier:profile:error:"
+ "_medicalRecordWithUUID:profile:error:"
+ "_predicateForDownloadableAttachmentsWithMedicalRecordIdentifier:"
+ "_processClinicalNotesType:medicalRecord:clinicalRecord:profile:error:"
+ "_reconcileExistingAttachmentsIfFoundForDownloadableAttachment:medicalRecord:clinicalRecord:attachment:profile:error:"
+ "_updateWithExistingAttachmentIfFoundForDownloadableAttachment:medicalRecord:clinicalRecord:profile:error:"
+ "attachmentSchemaIdentifier"
+ "didCompleteReExtractionWithCompletion:numExtracted:errorReturned:"
+ "hkAttachment"
+ "hk_firstSortedObjectWithComparison:"
+ "v40@0:8@?16@24@32"
- "%{public}@ %{public}@ did not insert because %{public}@"
- "%{public}@: _storeDataFromClinicalItem failed to retrieve stored record for uniqueness checksum with error: %{public}@"
- "Attachments only supported for ClinicalNoteRecord"
- "_attachmentIdentifierForMedicalRecordWithUUID:type:profile:error:"
- "_checkForObsoleteDownloadableAttachmentsForMedicalRecord:extractedDownloadableAttachments:accountIdentifier:medicalObjectIdentifier:clinicalObjectIdentifier:profile:error:"
- "_deleteAttachmentsWithMedicalRecordIdentifier:accountIdentifier:profile:error:"
- "_medicalRecordWithUUID:type:profile:error:"
- "_predicateForDownloadableAttachmentsWithAccountIdentifier:medicalRecordIdentifier:"
- "_processClinicalNotesType:attachmentObjectIdentifier:profile:error:"
- "_updateWithExistingAttachmentIfFoundForDownloadableAttachment:attachmentObjectIdentifier:profile:error:"
- "sortUsingComparator:"

```
