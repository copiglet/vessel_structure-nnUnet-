import nibabel as nib
import numpy as np

# Paths to the NIfTI files
ggo_consol_nifti_path = 'path_to_ggo_and_consolidation_mask_nifti_file.nii.gz'
vessel_nifti_path = 'path_to_vessel_structure_mask_nifti_file.nii.gz'

# Load the GGO and consolidation NIfTI file
ggo_consol_img = nib.load(ggo_consol_nifti_path)
ggo_consol_data = ggo_consol_img.get_fdata()

# Load the vessel structure NIfTI file
vessel_img = nib.load(vessel_nifti_path)
vessel_data = vessel_img.get_fdata()

# Subtract the vessel structure mask from the GGO and consolidation mask
# This assumes that the vessel mask is binary (1 for vessels, 0 for non-vessels)
separated_mask_data = ggo_consol_data - vessel_data
separated_mask_data[separated_mask_data < 0] = 0  # Remove negative values resulting from subtraction

# Save the separated mask as a new NIfTI image
separated_mask_img = nib.Nifti1Image(separated_mask_data, ggo_consol_img.affine, ggo_consol_img.header)
nib.save(separated_mask_img, 'separated_mask.nii.gz')

print("The vessel structures have been separated from the GGO and consolidation mask.")
