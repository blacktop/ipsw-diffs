## libSparse.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib`

```diff

-127.120.9.0.0
-  __TEXT.__text: 0xf3398
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__const: 0x548
-  __TEXT.__cstring: 0x3427
-  __TEXT.__oslogstring: 0x18bc
-  __TEXT.__gcc_except_tab: 0xca4
-  __TEXT.__unwind_info: 0x1018
+182.0.0.0.0
+  __TEXT.__text: 0x161b94
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__const: 0x760
+  __TEXT.__cstring: 0x4d1d
+  __TEXT.__oslogstring: 0x1c5d
+  __TEXT.__gcc_except_tab: 0xa4c
+  __TEXT.__unwind_info: 0x16c0
   __TEXT.__eh_frame: 0x8b0
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x8c0
-  __AUTH_CONST.__auth_got: 0x4f8
-  __AUTH_CONST.__const: 0x90
-  __AUTH.__thread_vars: 0x78
-  __AUTH.__thread_data: 0x4
-  __AUTH.__thread_bss: 0x6808
-  __DATA.__data: 0x4
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0xad0
+  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__const: 0x1d0
+  __AUTH.__thread_vars: 0xd8
+  __AUTH.__thread_data: 0xc
+  __AUTH.__thread_bss: 0x8818
+  __DATA.__data: 0x14
+  __DATA.__common: 0x98
+  __DATA.__bss: 0x12018
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: D9D779C2-1136-37A8-BB30-273FD88CF645
-  Functions: 1322
-  Symbols:   618
-  CStrings:  490
+  UUID: 5B0A37B2-4F8C-3C47-9C79-183D3DE6C9A4
+  Functions: 1896
+  Symbols:   676
+  CStrings:  694
 
Symbols:
+ _BLASGetThreading
+ _BLASSetThreading
+ __NSConcreteGlobalBlock
+ __SparseFactorSymmetric_Complex_Double
+ __SparseFactorSymmetric_Complex_Float
+ __SparseNumericFactorSymmetric_Complex_Double
+ __SparseNumericFactorSymmetric_Complex_Float
+ __SparseRefactorSymmetric_Complex_Double
+ __SparseRefactorSymmetric_Complex_Float
+ __Z23SparseWriteBinaryMatrixijPKcm18SparseMatrix_FloatP17DenseMatrix_FloatS3_
+ __Z23SparseWriteBinaryMatrixijPKcm19SparseMatrix_DoubleP18DenseMatrix_DoubleS3_
+ __Z23SparseWriteBinaryMatrixijPKcm26SparseMatrix_Complex_FloatP25DenseMatrix_Complex_FloatS3_
+ __Z23SparseWriteBinaryMatrixijPKcm27SparseMatrix_Complex_DoubleP26DenseMatrix_Complex_DoubleS3_
+ __Z28SparseReadBinaryMatrix_FloatPKcmjPPcPmb
+ __Z29SparseReadBinaryMatrix_DoublePKcmjPPcPmb
+ __Z34SparseReadBinaryAuxilaryData_FloatjPKcmjb
+ __Z35SparseReadBinaryAuxilaryData_DoublejPKcmjb
+ __Z36SparseReadBinaryMatrix_Complex_FloatPKcmjPPcPmb
+ __Z37SparseReadBinaryMatrix_Complex_DoublePKcmjPPcPmb
+ __Z42SparseReadBinaryAuxilaryData_Complex_FloatjPKcmjb
+ __Z43SparseReadBinaryAuxilaryData_Complex_DoublejPKcmjb
+ __ZnwmSt19__type_descriptor_t
+ ___memcpy_chk
+ ___sprintf_chk
+ _abort
+ _dispatch_once
+ _exp
+ _exp2
+ _expf
+ _fclose
+ _fopen
+ _ftruncate
+ _getenv
+ _getpid
+ _gettimeofday
+ _ioctl
+ _log
+ _logf
+ _madvise
+ _mmap
+ _munmap
+ _nrand48
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _perror
+ _pow
+ _pthread_cond_broadcast
+ _pthread_cond_destroy
+ _pthread_cond_init
+ _pthread_cond_signal
+ _pthread_cond_wait
+ _pthread_mutex_destroy
+ _pthread_mutex_init
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _pthread_qos_max_parallelism
+ _qos_class_self
+ _qsort_b
+ _strcmp
+ _system
+ _vm_page_size
- _APPLE_NTHREADS
- __Znwm
- _sched_yield
CStrings:
+ "\t\t\tContraction: %.05fs\n"
+ "\t\t\tMatching: %.05fs\n"
+ "\t\t\tProjection: %.05fs\n"
+ "\t\t\tRefinement: %.05fs\n"
+ "\t\tCoarsening: %.05fs\n"
+ "\t\tInitial Partitioning: %.05fs\n"
+ "\t\tMoving %6d from %3d to %3d [%6d %6d]. Gain: %4d. Cut: %6d\n"
+ "\t\tMoving %6d from %3d to %3d. Gain: [%4d %4d]. Cut: %6d, Vol: %6d\n"
+ "\t\tMoving %6d from %3d/%d to %3d/%d [%6d %6d]. Gain: %4d. Cut: %6d\n"
+ "\t\tMoving %6d to %3d. Gain: %4d. Cut: %6d\n"
+ "\t\tRecursion Overhead: %.05fs\n"
+ "\t\tScheme: %d. Moving to %d\n"
+ "\t\tUncoarsening: %.05fs\n"
+ "\t\tto=%d, nadd=%d, %d\n"
+ "\t***Cannot bisect a graph with 0 vertices!\n\t***You are trying to partition a graph into too many parts!"
+ "\tMetis: %.05fs\n"
+ "\tMinOut: %4d, to: %3d, TtlWgt: %5d[#:%d]\n"
+ "\tMoving it to %d [%d] [%d]\n"
+ "\tOrdering: %.05fs\n"
+ "\tPartitioning: %.05fs\n"
+ "\tPostprocessing: %.05fs\n"
+ "\tPreprocessing: %.05fs\n"
+ "\t[%6d %6d], Bal: %5.3f, Nb: %6d. Nmoves: %5d, Cut: %6d, Vol: %6d"
+ "\t[%6d %6d], Bal: %5.3f, Nb: %6d. Nmoves: %5d, Cut: %6d, Vol: %6d\n"
+ " \t\n"
+ "     constraint #0:  %5.3lf out of %5.3lf\n"
+ "     pid: %u, actual: %d, desired: %d, ratio: %.2lf\n"
+ "   Create contiguous partitions: %s\n"
+ "   On disk storage: %s\n"
+ "  Ipart Select bestobj: %d\n"
+ "  Ipart.%d curobj: %d\n"
+ "  nvtxs: %d, nmis: %d\n"
+ "  nvtxs: %d, nmis: %d, minvwgt: %d, ii: %d\n"
+ " - Balance:"
+ " - Edgecut: %d, communication volume: %u.\n\n"
+ " - Most overweight partition:"
+ " - Separator Size: %d.\n\n"
+ " size of vtx_type: %zu, adj_type: %zu, wgt_type: %zu, pid_type: %zu, tid_type: %zu, real_type: %zu\n"
+ "%.*s"
+ "%c "
+ "%s "
+ "%s: [%6d %6d %6d], Bal: %5.3f(%.3f), Nv-Nb[%6d %6d], Cut: %6d, (%d)"
+ "%s: [%6d %6d %6d], Bal: %5.3f(%.3f),, Nv-Nb[%6d %6d], Cut: %5d, Vol: %5d, (%d)"
+ "%s: [%6d %6d]-[%6d %6d], Bal: %5.3f, Nv-Nb[%6d %6d], Cut: %5d, Vol: %5d"
+ "%s: [%6d %6d]-[%6d %6d], Bal: %5.3f, Nv-Nb[%6d %6d], Cut: %6d"
+ "%zu) [%u %u] {%d %d %d # %d %u}\n"
+ "%zu) [%u %u] {%d %u}\n"
+ "%zu) [%u %u] {%d:%d %d # %d:%d %u}\n"
+ "***ASSERTION failed on line %d of file %s: ComputeCut(graph, where) == graph->mincut\n"
+ "***ASSERTION failed on line %d of file %s: k>=0\n"
+ ", Doms: [%3d %4d]"
+ "/Library/Caches/com.apple.xbs/Sources/Sparse/MTMetis/metis/libmetis/kwayfm.c"
+ "Adjacent Subdomain Stats: Total: %3d, Max: %3d[%zu], Avg: %3d\n"
+ "AllocateKWayPartitionMemory: bndind"
+ "AllocateKWayPartitionMemory: bndptr"
+ "AllocateKWayPartitionMemory: ckrinfo"
+ "AllocateKWayPartitionMemory: pwgts"
+ "AllocateKWayPartitionMemory: where"
+ "AllocateKWayVolPartitionMemory: vkrinfo"
+ "AllocateRefinementWorkSpace: adids"
+ "AllocateRefinementWorkSpace: adwgts"
+ "AllocateRefinementWorkSpace: cnbrpool"
+ "AllocateRefinementWorkSpace: maxnads"
+ "AllocateRefinementWorkSpace: nads"
+ "AllocateRefinementWorkSpace: pvec1"
+ "AllocateRefinementWorkSpace: pvec2"
+ "AllocateRefinementWorkSpace: vnbrpool"
+ "Balance: %0.2lf | Distribution: %s\n"
+ "Best Objective: %d\n"
+ "Cannot use SparseFactorizationCholesky for Complex symmetric matrices.\n"
+ "Coarsening Type: %s | Contraction Type: %s\n"
+ "Coarsest graph{%zu} has %u vertices, %u edges, and %lld exposed edge weight.\n"
+ "ComputeSubDomainGraph: adids[pid]"
+ "ComputeVolume: marker"
+ "DLTHREAD_POOL_SCHEDULE"
+ "Direct Bisection Partitioning"
+ "Direct k-way Partitioning"
+ "ERROR: "
+ "Failed during initial partitioning\n"
+ "Failed on writing %s\n"
+ "Failed to acquire chunkFactorStorage from pool\n"
+ "Failed to mmap file\n"
+ "Failed to resize file to length %llu\n"
+ "File format only supported with SparseReadBinaryMatrix_*\n"
+ "File format only supported with SparseReadMatrix_*\n"
+ "Final partition on graph %zu: %d cut and %5.4lf balance\n"
+ "Final partition on graph %zu: %d separator and %5.4lf balance\n"
+ "FindPartitionInducedComponents: cind"
+ "FindPartitionInducedComponents: cptr"
+ "FindPartitionInducedComponents: perm"
+ "FindPartitionInducedComponents: todo"
+ "FindPartitionInducedComponents: touched"
+ "FindPartitionInducedComponents: where"
+ "GBC"
+ "GBV"
+ "GRC"
+ "GRE: [%6d %6d]-[%6d %6d], Bal: %5.3f, Nv-Nb[%6d %6d], Cut: %6d\n"
+ "GRV"
+ "Graph{%zu} has %u[%u] vertices, %u edges, and %lld exposed edge weight.\n"
+ "I found %d components, for this %d-way partition\n"
+ "IncreaseEdgeSubDomainGraph: adids[pid]"
+ "InitKWayPartitioning: ubvec"
+ "Initial %d-way partitioning cut: %d\n"
+ "Initial Cut: %d\n"
+ "Invalid number of threads: %u\n"
+ "Leaf-Matching: %s | Remove Islands: %s\n"
+ "METIS Error: A contiguous partition is requested for a non-contiguous input graph.\n"
+ "MTMETIS TIME"
+ "Matrix is structurally rank deficient\n"
+ "Me: %d, Degree: %4d, TotalOut: %d,\n"
+ "Mean Objective - Geo.: %0.2lf - Ari.: %.2lf\n"
+ "Median Objective: %d\n"
+ "Metis returned '%d' during initial partitioning\n"
+ "Number %s not read correctly as %s\n"
+ "Number of Partitions: %u | Partition Type: %s\n"
+ "Number of Runs: %zu | Random Seed: %u\n"
+ "Number of Threads: %u | Verbosity: %s\n"
+ "PARAMETERS"
+ "Recursive Bisection Partitioning"
+ "Refinement Type: %s | Number of Refinement Passes: %zu\n"
+ "Refinement pass %zu: %d improvement\n"
+ "Refinement pass %zu: %u moves\n"
+ "STATISTICS"
+ "Selected initial partition with cut of %d\n"
+ "Selected initial partition with separator of %d\n"
+ "SparseScalingHungarianScalingAndOrdering is not supported for symmetric factorizations."
+ "Stopped at ntodo: %d\n"
+ "Symbolic workspace requirement calculation overflowed.\n"
+ "The graph is not connected. It has %d connected components.\n"
+ "The number of partitions must be at least 1.\n"
+ "The number of partitions must be specified.\n"
+ "Total Time: %.03fs\n"
+ "Trying to move %d [%d] from %d\n"
+ "Unknown contraction type '%d'\n"
+ "Unknown distribution '%d'\n"
+ "Unknown initial partition type: %d\n"
+ "Unknown iptype: %d\n"
+ "Unknown objtype %d\n"
+ "Unknown objtype of %d\n"
+ "Unknown objtype: %d\n"
+ "Unknown partition type '%d'\n"
+ "Unknown partitoin type '%d'\n"
+ "Unknown ptype '%d'"
+ "Unknown refinement type '%d'\n"
+ "Unknown refinement type for edge separators '%d'\n"
+ "Unknown scantype '%d'\n"
+ "Unknown timer state %d\n"
+ "Unsupported refinement type '%d' for K-Way partitions."
+ "VECLIB_MAXIMUM_THREADS"
+ "Vertex Separator"
+ "Worst Objective: %d\n"
+ "You just increased the maxndoms: %d %d\n"
+ "_SparseRefactorHermitian only applies to SparseHermitian matrices"
+ "_SparseRefactorSymmetric only applies to SparseSymmetric matrices"
+ "block"
+ "blockcyclic"
+ "cnbrpoolGet: cnbrpool"
+ "ctrl->tpwgts"
+ "cyclic"
+ "dense"
+ "esep"
+ "fc"
+ "fm"
+ "greedy"
+ "high"
+ "hs"
+ "i24@?0r^v8r^v16"
+ "kway"
+ "lfrf"
+ "lfrl"
+ "llrf"
+ "llrl"
+ "low"
+ "ls"
+ "maximum"
+ "medium"
+ "metis%d.%d"
+ "nd"
+ "nfoptions->scalingMethod=SparseScalingHungarianScalingAndOrdering is only supported if a combined symbolic+numeric call to SparseFactor() is made.\n"
+ "nfoptions.orderMethod=SparseScalingHungarianScalingAndOrdering is not supported with sfoptions.ignoreRowsAndColumns!=NULL\n"
+ "nfoptions.orderMethod=SparseScalingHungarianScalingAndOrdering is not supported with sfoptions.orderMethod==SparseOrderUser\n"
+ "nfoptions.orderMethod=SparseScalingHungarianScalingAndOrdering is only supported for blockSize=1\n"
+ "none"
+ "rb"
+ "rm"
+ "rm -r %s"
+ "sfg"
+ "sfm"
+ "shem"
+ "sort"
+ "v8@?0"
+ "vnbrpoolGet: vnbrpool"
+ "vsep"
+ "wb"
- "Symmetric matrices are not supported with complex-valued type (did you mean Hermitian?)\n"

```
