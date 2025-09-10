## KDKs

- `KDK_26.0_25A5349a.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_26.0_25A353.kdk/System/Library/Kernels/kernel.release.t6031`

#### _amfi

```diff

 amfi_query_context_to_object query_context_to_object;	
 TrustCacheInterface_t TrustCache;	
 OSEntitlementsInterface_t OSEntitlements;	
+amfi_has_mte_soft_mode has_mte_soft_mode;	
+amfi_has_mte_opt_out has_mte_opt_out;	
+amfi_has_mte_inheritance_opt_out has_mte_inheritance_opt_out;	
+amfi_has_mte_data_tagging_opt_in has_mte_data_tagging_opt_in;	
+amfi_has_mte_alias_restriction_opt_in has_mte_alias_restriction_opt_in;	
 }

```
