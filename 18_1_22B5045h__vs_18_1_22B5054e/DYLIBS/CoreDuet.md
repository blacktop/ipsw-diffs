## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1888.0.0.0.0
-  __TEXT.__text: 0x1958dc
+1891.0.1.0.0
+  __TEXT.__text: 0x197540
   __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_methlist: 0x103b0
-  __TEXT.__cstring: 0x15c9b
+  __TEXT.__objc_methlist: 0x103f8
+  __TEXT.__cstring: 0x15dd6
   __TEXT.__const: 0x5b8
-  __TEXT.__oslogstring: 0x17be4
-  __TEXT.__gcc_except_tab: 0x7d94
+  __TEXT.__oslogstring: 0x17e6d
+  __TEXT.__gcc_except_tab: 0x7df4
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x5500
+  __TEXT.__unwind_info: 0x5570
   __TEXT.__objc_classname: 0x2c6e
-  __TEXT.__objc_methname: 0x25fc2
+  __TEXT.__objc_methname: 0x2609e
   __TEXT.__objc_methtype: 0x615a
-  __TEXT.__objc_stubs: 0x17080
-  __DATA_CONST.__got: 0x1170
-  __DATA_CONST.__const: 0x3af8
+  __TEXT.__objc_stubs: 0x17160
+  __DATA_CONST.__got: 0x1178
+  __DATA_CONST.__const: 0x3b38
   __DATA_CONST.__objc_classlist: 0xc38
-  __DATA_CONST.__objc_catlist: 0x70
+  __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ed0
+  __DATA_CONST.__objc_selrefs: 0x7f10
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x6a8
   __DATA_CONST.__objc_arraydata: 0x6e8
   __AUTH_CONST.__auth_got: 0xa70
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x1be0
-  __AUTH_CONST.__cfstring: 0x133c0
-  __AUTH_CONST.__objc_const: 0x25750
+  __AUTH_CONST.__const: 0x1c80
+  __AUTH_CONST.__cfstring: 0x13400
+  __AUTH_CONST.__objc_const: 0x25790
   __AUTH_CONST.__objc_intobj: 0x23b8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x5e8

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8499
-  Symbols:   10777
-  CStrings:  11871
+  Functions: 8528
+  Symbols:   10808
+  CStrings:  11899
 
Symbols:
+ __CDTargetBundleIdForBundleId
+ _OBJC_CLASS_$_NSBatchInsertRequest
CStrings:
+ "Knowledge store has been decomissioned"
+ "T@\"NSDate\",C,N,V_firstIncomingSenderDate"
+ "T@\"NSDate\",C,N,V_lastIncomingRecipientDate"
+ "initWithObjects:forKeys:"
+ "DecomissionKnowledgeStoreFault"
+ "dataWithPropertyList:format:options:error:"
+ "DecomissionKnowledgeStore"
+ "-executeQuery:responseQueue: dropped. Knowledge store has been decomissioned."
+ "serialized != nil"
+ "T@\"NSDate\",C,N,V_lastOutgoingRecipientDate"
+ "metadata: failed to set get key %!{(MISSING)public}@: %!{(MISSING)private}@"
+ "Handling callback for %!{(MISSING)public}s"
+ "metadata: failed to set delete key %!{(MISSING)public}@: %!{(MISSING)private}@"
+ "initWithEntity:objects:"
+ "Learning toggled. New disabled: %!{(MISSING)public}@. New enabled: %!{(MISSING)public}@"
+ "metadata: failed to set %!{(MISSING)private}@ for key %!{(MISSING)public}@: %!{(MISSING)private}@"
+ "allDisabledBundles equals persistedDisabledBundles (%!{(MISSING)public}@); bailing"
+ "-[_CDInteractionStore setMetadata:forKey:]_block_invoke"
+ "T@\"NSDate\",C,N,V_firstOutgoingRecipientDate"
+ "_CDInteractionStore.m"
+ "SELF.bundleId IN %!@(MISSING) OR SELF.targetBundleId IN %!@(MISSING)"
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "bundleId == %!@(MISSING) OR targetBundleId = %!@(MISSING)"
+ "Metadata"
+ "metadata: failed to load metadataDictionary: %!{(MISSING)private}@"
+ "Deleted %!t(MISSING)u objects for newly-disabled learning bundles: %!{(MISSING)public}@"
+ "T@\"NSDate\",C,N,V_lastIncomingSenderDate"
+ "T@\"NSDate\",C,N,V_firstIncomingRecipientDate"
+ "metadataDictionary"
+ "-deviceUUID: returning nil. Knowledge store has been decomissioned."
+ "_deleteMetadataForKey:moc:"
+ "Failed to delete objects for disabled learning bundles: %!{(MISSING)public}@"
+ "metadataForKey:"
+ "_cd_containsSiriLearningBundleId:"
+ "Deleted %!t(MISSING)u interactions for newly-disabled learning bundle: %!{(MISSING)public}@"
+ "setMetadata:forKey:"
+ "(bundleId == %!@(MISSING) OR targetBundleId == %!@(MISSING)) AND account == %!@(MISSING)"
+ "Filtered %!t(MISSING)u interactions for bundles with Siri Learning disabled (%!{(MISSING)public}@)"
+ "key = %!@(MISSING)"
+ "CoreDuet"
+ "Failed to delete interactions for disabled learning bundle: %!{(MISSING)public}@"
+ "newly disabled bundle %!{(MISSING)public}@ is already in persistedDisabledBundles; skipping"
+ "v24@?0@\"NSArray\"8@\"NSArray\"16"
- "Learning toggled. New disabled: %!@(MISSING). New enabled: %!@(MISSING)"
- "T@\"NSDate\",&,V_firstIncomingRecipientDate"
- "T@\"NSDate\",&,V_lastIncomingSenderDate"
- "startSanitizingInteractionStore (newDisabledBundles=%!@(MISSING))"
- "bundleId == %!@(MISSING) AND account == %!@(MISSING)"
- "T@\"NSDate\",&,V_firstOutgoingRecipientDate"
- "Failed to delete interactions for disabled learning bundles: %!@(MISSING)"
- "SELF.bundleId IN %!@(MISSING)"
- "Failed to delete objects for disabled learning bundles: %!@(MISSING)"
- "Handling callback for %!@(MISSING)"
- "Deleted %!@(MISSING) objects for newly-disabled learning bundles: %!@(MISSING)"
- "T@\"NSDate\",&,V_lastOutgoingRecipientDate"
- "T@\"NSDate\",&,V_firstIncomingSenderDate"
- "T@\"NSDate\",&,V_lastIncomingRecipientDate"
- "Filtered interactions for bundles with Siri Learning disabled: %!@(MISSING)"
- "Deleted %!@(MISSING) interactions for newly-disabled learning bundles: %!@(MISSING)"

```
