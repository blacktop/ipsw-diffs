## KDKs

- `KDK_14.6_23G5052d.kdk/System/Library/Kernels/kernel.release.t6031`
- `KDK_14.6_23G5061b.kdk/System/Library/Kernels/kernel.release.t6031`

#### recount_processor

```diff

 struct recount_processor {
 struct recount_snap rpr_snap;	
 struct recount_track rpr_active;	
-struct recount_snap rpr_interrupt_snap;	
-uint64_t rpr_interrupt_time_mach;	
+uint64_t rpr_interrupt_duration_mach;	
+uint64_t rpr_last_interrupt_enter_time_mach;	
+uint64_t rpr_last_interrupt_leave_time_mach;	
 uint64_t rpr_idle_time_mach;	
 uint64_t rpr_state_last_abs_time;	
 uint8_t rpr_cpu_kind_index;	

```
#### recount_thread

```diff

 struct recount_thread {
 struct recount_track* rth_lifetime;	
-uint64_t rth_interrupt_time_mach;	
+uint64_t rth_interrupt_duration_mach;	
 recount_level_t rth_current_level;	
 }

```
