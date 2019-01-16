'''
Point cloud class generated from stereo image pairs.

Classes:

    * ``PointCloud`` - Point cloud with RGB colors

.. image:: classes_point_cloud.svg
'''

import numpy as np


class PointCloud(object):

    """3D point cloud generated from a stereo image pair."""

    #: Header for exporting point cloud to PLY
    ply_header = (
'''ply
format ascii 1.0
element vertex {vertex_count}
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
end_header
''')

    def __init__(self, coordinates, colors):
        """
        Initialize point cloud with given coordinates and associated colors.

        ``coordinates`` and ``colors`` should be numpy arrays of the same
        length, in which ``coordinates`` is made of three-dimensional point
        positions (X, Y, Z) and ``colors`` is made of three-dimensional spectral
        data, e.g. (R, G, B).
        """
        self.coordinates = coordinates.reshape(-1, 3)
        self.colors = colors.reshape(-1, 3)

    def write_ply(self, output_file):
        """Export ``PointCloud`` to PLY file for viewing in MeshLab."""
        points = np.hstack([self.coordinates, self.colors])
        with open(output_file, 'w') as outfile:
            outfile.write(self.ply_header.format(
                                            vertex_count=len(self.coordinates)))
            np.savetxt(outfile, points, '%f %f %f %d %d %d')

    def filter_infinity(self):
        """Filter infinite distances from ``PointCloud.``"""
        mask = self.coordinates[:, 2] > self.coordinates[:, 2].min()
        coords = self.coordinates[mask]
        colors = self.colors[mask]
        return PointCloud(coords, colors)
