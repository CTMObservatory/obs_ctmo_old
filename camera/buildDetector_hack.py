import lsst.afw.table as afwTable
import numpy as np

# Gain: (0.722 pm 0.006) ADU/electron
gain = 0.722
# Readout noise: (15.8 pm 0.2) ADU
readout_noise = 15.8
# Saturation level: 65535 ADU
saturation = 65535

sample_fits_path = "subaru_hsc_camera_0_00.fits"
hscAfw = afwTable.BaseCatalog.readFits(sample_fits_path)
ctmoAfw = hscAfw[:1]

# Change the pixel coord stuff for every ccd
h, w = 4096, 4096
ctmoAfw["bbox_extent_x"] = w
ctmoAfw["bbox_extent_y"] = h
ctmoAfw["raw_bbox_extent_x"] = w
ctmoAfw["raw_bbox_extent_y"] = h
ctmoAfw["raw_databbox_min_x"] = 0
ctmoAfw["raw_databbox_min_y"] = 0
ctmoAfw["raw_databbox_extent_x"] = w
ctmoAfw["raw_databbox_extent_y"] = h
ctmoAfw["raw_horizontaloverscanbbox_min_x"] = 0
ctmoAfw["raw_horizontaloverscanbbox_min_y"] = 0
ctmoAfw["raw_horizontaloverscanbbox_extent_x"] = 0
ctmoAfw["raw_horizontaloverscanbbox_extent_y"] = 0
ctmoAfw["raw_verticaloverscanbbox_min_x"] = 0
ctmoAfw["raw_verticaloverscanbbox_min_y"] = 0
ctmoAfw["raw_verticaloverscanbbox_extent_x"] = 0
ctmoAfw["raw_verticaloverscanbbox_extent_y"] = 0
ctmoAfw["raw_prescanbbox_min_x"] = 0
ctmoAfw["raw_prescanbbox_min_y"] = 0
ctmoAfw["raw_prescanbbox_extent_x"] = 0
ctmoAfw["raw_prescanbbox_extent_y"] = 0

ctmoAfw["gain"] = gain
ctmoAfw["linearity_coeffs"] = [1.0, np.nan, np.nan, np.nan]
ctmoAfw["readnoise"] = readout_noise
ctmoAfw["saturation"] = saturation
ctmoAfw.writeFits("PL16803.fits")

# record.setHasRawInfo(True) #Sets the first Flag=True
# record.setRawFlipX(False)  #Sets the second Flag=False
# record.setRawFlipY(False)  #Sets the third Flag=False
# record.setBBox(bbox)
# record.setName('left' if i == 0 else 'right')
# record.setGain(gain)
# record.setSaturation(saturation)
# record.setReadNoise(readNoise)
# record.setReadoutCorner(readoutCorner)
# record.setLinearityCoeffs(linearityCoeffs)
# record.setLinearityType(linearityType)
# record.setRawBBox(rawBBox)
# record.setRawXYOffset(rawXYOffset)
# record.setRawDataBBox(rawDataBBox)
# record.setRawHorizontalOverscanBBox(rawHorizontalOverscanBBox)
# record.setRawVerticalOverscanBBox(emptyBox)
# record.setRawPrescanBBox(emptyBox)
