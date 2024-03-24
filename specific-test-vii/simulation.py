from lenstronomy.LensModel.lens_model import LensModel
from lenstronomy.Plots import lens_plot
import matplotlib.pyplot as plt
import numpy as np
import warnings


# Einstein angle
def theta_Einstein(m: float, d_s: float, d_l: float) -> float:
    d_ls = d_s - d_l
    return np.sqrt(m * 1e-11) / np.sqrt(d_l * d_s / d_ls)

def main() -> None:
    warnings.filterwarnings('ignore')
    mass, dist_s = 1e12, 10

    m = input('Mass of the lense in Sun masses: ')
    try:
        mass = float(m)
    except:
        print('Using default mass')
    
    d = input('Distance to the source in Gpc: ')
    try:
        dist_s = float(d)
    except:
        print('Using default distance')

    # lense distance is half of the source distance
    dist_l = 0.5 * dist_s
    theta_E = theta_Einstein(mass, dist_s, dist_l) 

    lens_model_list = ['POINT_MASS']
    lensModel = LensModel(lens_model_list=lens_model_list)
    kwargs_lens = [{'theta_E': theta_E, 'center_x': 0, 'center_y': 0}]

    theta_ra, theta_dec = 1.0, 0.5 # some fixed sky coordinates
    beta_ra, beta_dec = lensModel.ray_shooting(
        theta_ra, theta_dec, kwargs_lens
    )

    kwargs_lens_plot = {
        'with_caustics': True, 'fast_caustic': True,
        'point_source': True, 'coord_inverse': False
    }
    f, ax = plt.subplots(1, 1, figsize=(10, 8), sharex=False, sharey=False)
    lens_plot.lens_model_plot(
        ax, lensModel=lensModel, kwargs_lens=kwargs_lens, 
        sourcePos_x=beta_ra, sourcePos_y=beta_dec, **kwargs_lens_plot
    )
    ax.set_title(
        rf'Point Mass Lensing Simulation, $M$ = {mass:.1E} $M_\odot$, '
        rf'$D_S$ = {dist_s} Gpc'
    )
    ax.set_xlabel(
        r'$\theta_{RA}$ = 'f'{theta_ra} arcsec, '
        r'$\theta_{DEC}$ = 'f'{theta_dec} arcsec'
    )
    plt.tight_layout()
    plt.savefig('specific-test-vii/point_mass_grav_lense.png', dpi=500)

if __name__ == '__main__':
    main()